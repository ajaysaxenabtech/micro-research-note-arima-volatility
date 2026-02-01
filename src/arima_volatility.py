"""ARIMA + volatility-regime utilities for the micro research note.

Designed for quick, readable use inside the notebook:
- compute returns + rolling volatility
- select windows (manual)
- small-grid ARIMA order selection using AIC
- forecast + error metrics
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple, Optional, Iterable

import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def compute_returns(nav: pd.Series, kind: str = "log") -> pd.Series:
    """Compute 1-step returns from NAV levels."""
    nav = nav.astype(float)
    if kind == "log":
        return np.log(nav).diff()
    if kind == "simple":
        return nav.pct_change()
    raise ValueError("kind must be 'log' or 'simple'")


def rolling_volatility(returns: pd.Series, window: int) -> pd.Series:
    """Rolling standard deviation of returns."""
    return returns.rolling(window=window, min_periods=window).std()


def mape(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    eps = 1e-12
    return float(np.mean(np.abs((y_true - y_pred) / (y_true + eps))) * 100.0)


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return float(np.mean(np.abs(y_true - y_pred)))


@dataclass
class ArimaSelectionResult:
    order: Tuple[int, int, int]
    aic: float


def select_arima_order_aic(
    y: pd.Series,
    p_values: Iterable[int] = range(0, 4),
    d_values: Iterable[int] = range(0, 3),
    q_values: Iterable[int] = range(0, 4),
) -> ArimaSelectionResult:
    """Select ARIMA(p,d,q) with lowest AIC over a small grid.

    Notes:
    - Keep the grid small for a micro note.
    - Some combinations may fail; they are skipped.
    """
    best_order = None
    best_aic = np.inf

    y = y.astype(float).dropna()

    for p in p_values:
        for d in d_values:
            for q in q_values:
                try:
                    model = ARIMA(y, order=(p, d, q))
                    res = model.fit()
                    aic = float(res.aic)
                    if aic < best_aic:
                        best_aic = aic
                        best_order = (p, d, q)
                except Exception:
                    continue

    if best_order is None:
        raise RuntimeError("No ARIMA model converged in the provided grid. Reduce grid or check data.")

    return ArimaSelectionResult(order=best_order, aic=best_aic)


def fit_forecast_evaluate(
    y: pd.Series,
    horizon: int,
    order: Tuple[int, int, int],
) -> Dict[str, float]:
    """Fit ARIMA on train, forecast horizon, compute MAE/RMSE/MAPE."""
    y = y.astype(float).dropna()
    if len(y) <= horizon + 10:
        raise ValueError("Window too short. Increase L or reduce horizon.")

    train = y.iloc[:-horizon]
    test = y.iloc[-horizon:]

    model = ARIMA(train, order=order)
    res = model.fit()
    forecast = res.forecast(steps=horizon)

    y_true = test.values
    y_pred = np.asarray(forecast.values, dtype=float)

    return {
        "mae": mae(y_true, y_pred),
        "rmse": rmse(y_true, y_pred),
        "mape_pct": mape(y_true, y_pred),
    }
