# Micro Research Note — ARIMA vs Volatility Regime (Pension NAV)

This repository is a **mini-template** for a 2–3 page micro research note:

**Title:** Effect of Market Volatility on ARIMA Forecasting Accuracy for Pension NAV Time Series  
**Author:** Ajay Saxena (ORCID: 0009-0002-2479-2658)

## What you will produce (end-to-end)
1. A small, reproducible ARIMA experiment comparing two regimes (**Normal vs Volatile**)  
2. One results table (MAE/RMSE/MAPE) + one figure (Actual vs Forecast)  
3. A 3-page research note in `paper/` (DOCX; convert to PDF when ready)  

## Quick start (VS Code + Jupyter)
### 1) Put your data
Save a CSV to `data/nav.csv` with columns:
- `date` (YYYY-MM-DD)
- `nav` (numeric NAV)

See `data/README.md` for details.

### 2) Create environment
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
```

### 3) Run the notebook
Open:
- `notebooks/01_arima_volatility_micro_note.ipynb`

Run cells top-to-bottom. Outputs:
- `output/metrics_table.csv`
- `figures/figure1_actual_vs_forecast.png`

### 4) Fill the micro note
Open:
- `paper/micro_research_note_template_ajay_saxena.docx`

Copy:
- numbers from `output/metrics_table.csv` into **Table 1**
- the figure from `figures/` into **Figure 1**

## Suggested “publish” route (simple)
- Push this repo to GitHub
- Upload the final PDF to Zenodo and link the GitHub repo

## License
MIT (see `LICENSE`).
