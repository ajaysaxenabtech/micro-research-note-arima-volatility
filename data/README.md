DOI (v1.2): 10.5281/zenodo.18449920
DOI (all versions): 10.5281/zenodo.18449919

How to cite:
Saxena, A. (2026). Effect of Market Volatility on ARIMA Forecasting Accuracy for Pension NAV Time Series (Micro Research Note v1.2). Zenodo. 10.5281/zenodo.18449920

“Reproducibility” note:

data source is Axis Pension Fund website (do not redistribute raw data if terms restrict)

instructions to re-download the dataset


# Data

- `data/nav.csv`

## Required columns
- `date` : YYYY-MM-DD (or parseable by pandas)
- `nav`  : numeric NAV level

## Example
date,nav
2021-01-01,100.12
2021-01-02,100.25

## Notes
- If you have multiple funds, start with ONE series for the micro note.
- If your data is daily and has missing market days, that is fine.
