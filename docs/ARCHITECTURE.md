# 🏗️ Project Architecture

## Overview
This project follows a clean, modular architecture with separation of concerns:

```
Data Flow:
CSV File → Load → Clean → Validate → Analyze → JSON → Dashboard
```

## Components

### 1. Data Layer (`src/analysis.py`)
- Load CSV files
- Clean and transform data
- Calculate metrics and aggregations
- Export to JSON format

### 2. Validation Layer (`src/data_validator.py`)
- Check data quality
- Detect missing values
- Identify anomalies
- Generate quality reports

### 3. Utilities (`src/utils.py`)
- Helper functions
- Currency formatting
- File I/O operations

### 4. Presentation Layer (`dashboard/`)
- HTML5 structure
- CSS3 styling
- JavaScript interactivity
- Chart.js visualizations

## Key Metrics Calculated

1. **KPIs** - Revenue, Profit, Margin, Orders, AOV
2. **Time Series** - Monthly trends
3. **Category Analysis** - Revenue and profit by category
4. **Regional Analysis** - Performance by region
5. **Segment Analysis** - Customer segment breakdown
6. **Product Analysis** - Top performers
7. **Seasonality** - Monthly patterns

## Data Flow Example

```python
# 1. Load data
df = pd.read_csv('superstore_sales.csv')

# 2. Clean dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 3. Calculate metrics
revenue = df['Sales'].sum()
profit = df['Profit'].sum()
margin = (profit / revenue) * 100

# 4. Group and aggregate
category_data = df.groupby('Product Category').agg({
    'Sales': 'sum',
    'Profit': 'sum'
})

# 5. Export to JSON
json.dump(metrics, 'dashboard_data.json')
```

## Technology Stack

- **Backend:** Python 3, Pandas
- **Frontend:** HTML5, CSS3, JavaScript
- **Charting:** Chart.js
- **Testing:** Pytest, Unittest

## File Structure

```
src/
├── analysis.py          # Main analysis logic
├── data_validator.py    # Data quality checks
└── utils.py            # Helper functions

tests/
└── test_analysis.py    # Unit tests

dashboard/
├── index.html          # Main page
├── styles.css          # Styling
└── script.js           # JavaScript logic

data/
├── superstore_sales.csv # Raw data
└── dashboard_data.json  # Generated metrics

docs/
├── ARCHITECTURE.md     # This file
├── METHODOLOGY.md      # Analysis approach
└── DATA_QUALITY.md     # Data quality report
```
