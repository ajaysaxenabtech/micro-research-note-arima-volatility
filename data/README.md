# Data

Place your NAV time series at:

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
