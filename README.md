# XAUUSD Data Analysis

[![CI](https://github.com/KumailAbbas05/XAUUSD-Data-Analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/KumailAbbas05/XAUUSD-Data-Analysis/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)

A beginner-friendly financial-data analysis project built around a clearly labeled **synthetic XAUUSD demo dataset**.

## Project Goals

- Load and inspect OHLCV-style data
- Convert and sort dates
- Calculate daily percentage returns
- Visualize closing prices
- Practice financial-data analysis with Python
- Create a base for future work using real market data

## Dataset

The included file contains **120 synthetic daily observations** with:

- Date
- Open
- High
- Low
- Close
- Volume

> This is generated practice data, not real XAUUSD historical market data. No trading conclusions should be drawn from it.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Structure

```text
XAUUSD-Data-Analysis/
├── data/
│   ├── README.md
│   └── xauusd_synthetic_demo.csv
├── notebooks/
│   └── xauusd_analysis.ipynb
├── src/
│   └── analysis.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Run the Project

```bash
pip install -r requirements.txt
python src/analysis.py
```

You can also open `notebooks/xauusd_analysis.ipynb` for an interactive version.

## What I Practiced

- Reading CSV data with Pandas
- Working with dates
- Sorting time-series data
- Calculating percentage returns
- Plotting price data
- Organizing a data-analysis repository

## Next Steps

- Replace synthetic data with a real public XAUUSD dataset
- Add moving averages
- Add volatility analysis
- Compare XAUUSD with DXY data
- Add technical indicators
- Experiment with ML feature engineering

## Author

**Kumail Abbas**  
BS Artificial Intelligence Student
