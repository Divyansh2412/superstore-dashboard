
# Superstore Sales Dashboard

## Project Overview
This project creates an interactive sales dashboard for a superstore dataset. It features key performance indicators (KPIs), sales trends over time, and category-wise sales analysis.

## Features
- Monthly sales trends visualization
- Sales breakdown by product category
- Interactive dashboard built with Streamlit and Plotly

## Dataset
Uses a sales dataset with columns like `Order ID`, `Order Date`, `Category`, `Sales`, and more.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
````

### 2. Run exploratory analysis

```bash
python scripts/eda.py
```

### 3. Launch Streamlit dashboard

```bash
streamlit run scripts/dashboard.py
```

## Project Structure

```
superstore_dashboard/
├── data/                  # Sales dataset CSV
├── notebooks/             # Jupyter notebook for EDA
├── scripts/               # Python scripts
├── requirements.txt       # Python packages
└── README.md              # This file
```

## Author

Divyansh Miyan Bazaz

## License

MIT License
