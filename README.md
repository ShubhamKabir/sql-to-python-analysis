# SQL to Python: Sales Analysis Pipeline

This project demonstrates the transition from SQL-based querying to a Python-driven analytical workflow. It focuses on automating data cleaning, feature engineering, and visualization.

## Key Features
- **Data Integrity**: Automated handling of nulls and duplicates.
- **Feature Engineering**: Logic-based categorization of order values.
- **Time-Series Analysis**: Dynamic grouping by month names for trend reporting.
- **Visualization**: Professional-grade distribution charts.

## Insights Derived
- Identified NYC as the primary revenue driver (45% of total).
- Discovered high revenue dependency on a small group of repeat customers.
- Noted a significant gap between high-volume accessory sales and low revenue contribution.

## Setup
1. `pip install pandas matplotlib`
2. Run `python 01_setup_data.py`
3. Run `python 02_analysis_pipeline.py`