# Business Sales Analytics - Future Interns Task 1

A simple data analysis project to understand sales patterns and business performance.

## What does this do?

Analyzes 4 years of superstore sales data to find:
- Total revenue and profit
- Which categories/regions sell the most
- Which products are top sellers
- Revenue trends over time

## Quick Start

1. Install pandas:
```
pip install pandas openpyxl
```

2. Run the analysis:
```
python analysis.py
```

3. Open dashboard.html in browser

## What's in the project?

- `analysis.py` - Main script that reads data and calculates metrics
- `superstore_clean.csv` - Sales data (2009-2012)
- `dashboard_data.json` - Results (auto-generated)
- `dashboard.html` - Interactive charts

## Key Findings

1. **Technology** is most profitable (14.8% margin)
2. **Furniture** has low margins even though it sells well (2.3%)
3. **Tables** and **Bookcases** actually lose money
4. **Ontario and Prairie** regions perform best
5. **Corporate** customers bring most profit
6. Sales peak in **December**, low in **June**

## How it works

1. Load CSV file with pandas
2. Convert dates and clean data
3. Calculate revenue, profit, margins for different categories
4. Group by region, segment, products
5. Export results to JSON
6. Dashboard reads JSON and shows charts

## Files Explained

**analysis.py:**
- Reads the CSV file
- Calculates all the metrics (revenue, profit, margins)
- Groups data by category, region, customer segment
- Finds top 10 products
- Exports everything to JSON format

**dashboard.html:**
- Shows 5 KPI cards (revenue, profit, margin, orders, avg order value)
- 6 interactive charts using Chart.js
- Table of top products
- Business insights section
- All data comes from dashboard_data.json

## Data Fields

- Order Date - When order was placed
- Sales - Revenue amount
- Profit - Profit amount
- Product Category - What type (Technology, Furniture, Office Supplies)
- Region - Where it was sold
- Customer Segment - Type of customer (Corporate, Consumer, etc)

## Results

| Metric | Value |
|--------|-------|
| Total Revenue | ₹1,49,15,600 |
| Total Profit | ₹15,21,768 |
| Profit Margin | 10.2% |
| Orders | 5,496 |
| Avg Order Value | ₹2,713.90 |

## If something doesn't work

**"File not found"** - Make sure superstore_clean.csv is in same folder as analysis.py

**"pandas not found"** - Run: pip install pandas

**"Dashboard is blank"** - Run analysis.py first, then refresh browser

## Notes

- Data is from 2009-2012 (4 years)
- 8,399 total orders
- Indian superstore (regions are Canadian regions in this case)
- All numbers in rupees

Made for Future Interns Data Science Task 1
