# Effect of Market Volatility on ARIMA Forecasting Accuracy for Pension NAV Time Series (Micro Research Note v1.2)

**Zenodo DOI (v1.2):** https://doi.org/10.5281/zenodo.18449920  
**Zenodo DOI (all versions):** https://doi.org/10.5281/zenodo.18449919  

## How to cite
Saxena, A. (2026). *Effect of Market Volatility on ARIMA Forecasting Accuracy for Pension NAV Time Series* (Micro Research Note v1.2). Zenodo. https://doi.org/10.5281/zenodo.18449920

## What this repository contains
This repo reproduces the experiment behind the micro research note:
- Volatility proxy: rolling std. dev. of returns (**VOL_WINDOW=20**)
- Forecast horizon: **HORIZON=12**
- Regimes (N=60 each):
  - Normal: 2023-04-26 to 2023-07-21
  - Volatile: 2024-04-02 to 2024-07-03
- Model: ARIMA(p,d,q), order selected by AIC within each regime

## Reproducibility and data note
- **Data source:** Axis Pension Fund website (daily NAV)  
- **Important:** Do not redistribute raw NAV data if the website terms restrict redistribution.

### Data format expected
Create: `data/nav.csv` with columns:
- `date` (YYYY-MM-DD)
- `NAV` (numeric)

Example:
```csv
date,NAV
2022-10-25,9.8234
2022-10-26,9.8450


python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt


