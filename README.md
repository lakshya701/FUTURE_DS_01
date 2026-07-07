# 📊 Business Sales Analytics  
**Future Interns Data Science Task 1**

---

## 🎯 What This Project Does

I analyzed 4 years of superstore sales data (8,399 orders) to answer real business questions:
- Which products make the most money?
- How do sales change month to month?
- Which regions are most profitable?
- Where should we focus to grow?

Think of it like analyzing a retail shop's performance to decide what to sell more of.

---

## 👤 About Me

**Name:** Lakshya Agarwal  
**Intern ID:** FIT/JUN26/DS20521  
**Year:** 2nd CSE  
**Program:** Future Interns Data Science & Analytics

---

## 📂 How Files Are Organized

```
FUTURE_DS_01/
├── README.md                    ← You are here
├── requirements.txt             ← What Python packages you need
│
├── src/                        ← The main code
│   ├── analysis.py             ← Reads data and calculates everything
│   ├── data_validator.py        ← Checks if data is clean
│   └── utils.py                ← Helper functions
│
├── tests/                      ← Tests to verify code works
│   └── test_analysis.py
│
├── data/
│   ├── superstore_sales.csv    ← Raw data file
│   └── dashboard_data.json     ← Generated results
│
└── dashboard/
    ├── index.html              ← Open this in browser
    ├── styles.css              ← Styling
    └── script.js               ← Makes charts interactive
```

---

## 🚀 Quick Start (2 Minutes)

### Step 1: Install Python packages
```bash
pip install pandas openpyxl pyyaml
```

### Step 2: Run the analysis
```bash
python src/analysis.py
```

### Step 3: View the dashboard
Open `dashboard/index.html` in your browser. Done! 🎉

---

## 📊 The Data

**Dataset:** Superstore Sales (2009-2012)  
**Records:** 8,399 orders  
**What it has:**
- Order date and ID
- Product category (Technology, Furniture, Office Supplies)
- Sales amount (in rupees)
- Profit earned
- Region (West, Ontario, Prairie, etc)
- Customer type (Corporate, Consumer, Small Business)

---

## 💡 What I Found

### 1. Technology is the Star 🌟
- Technology products have 14.8% profit margin
- Furniture has only 2.3% margin (bad!)
- **What to do:** Sell more technology products

### 2. Some Products Lose Money 📉
- Tables lose ₹99,000 overall
- Bookcases lose ₹34,000
- **What to do:** Either increase price or find cheaper suppliers

### 3. Ontario Performs Best 👑
- Ontario has 11.3% profit margin
- West region has only 8.3% (despite more sales)
- **What to do:** Learn from Ontario, apply to other regions

### 4. Corporate Customers Are Valuable 💎
- Corporate brings ₹60 lakh profit
- Other segments bring only ₹30 lakh each
- **What to do:** Focus on keeping corporate customers happy

### 5. December & January Are Peak Months 🎄
- December: ₹1.47 crore (highest)
- June: ₹1.03 crore (lowest)
- **What to do:** Stock more for holiday season

---

## 🔍 How The Code Works

### `analysis.py` - The Main Script

This script does everything:
1. **Load data** → Read the CSV file
2. **Clean data** → Fix date formats, check for errors
3. **Calculate metrics** → Revenue, profit, margins by category/region
4. **Export results** → Save to JSON for the dashboard

Example function:
```python
def calculate_revenue(df):
    return df["Sales"].sum()  # Add all sales together
```

### `data_validator.py` - Quality Check

Checks if the data is good:
- Any missing values?
- Any negative numbers that shouldn't be?
- Any duplicate orders?

### Dashboard - The Interactive Part

When you open `index.html`, it:
- Shows 6 different charts
- Lets you see exact numbers when you hover
- Displays all the findings beautifully

---

## 🧪 Testing

Run tests to make sure everything works:
```bash
pip install pytest
pytest tests/
```

---

## 📈 Key Numbers

| Metric | Value |
|--------|-------|
| Total Revenue | ₹1.49 crore |
| Total Profit | ₹15.2 lakh |
| Orders | 5,496 |
| Profit Margin | 10.2% |
| Period | 2009-2012 |

---

## 🐛 If Something Goes Wrong

**Problem:** "File not found"  
**Fix:** Make sure `superstore_sales.csv` is in the `data/` folder

**Problem:** "pandas not found"  
**Fix:** Run `pip install pandas`

**Problem:** Dashboard is blank  
**Fix:** Run `python src/analysis.py` first, then refresh the webpage

---

## 💻 Technology Used

- **Python 3** - For data analysis
- **Pandas** - For reading and organizing data
- **HTML/CSS/JavaScript** - For the dashboard
- **Chart.js** - For making pretty charts

---

## 🎓 What I Learned

Working on this project taught me:
- ✅ How to clean messy data
- ✅ How to find patterns and insights
- ✅ How to present findings visually
- ✅ How real businesses use data to make decisions

---

## 📚 If You Want to Learn More

Check out:
- `docs/METHODOLOGY.md` - How I did the analysis
- `docs/DATA_QUALITY.md` - Details about the data
- `docs/ARCHITECTURE.md` - How different parts connect

---

## ✅ What's Complete

- [x] Data analysis done
- [x] All metrics calculated
- [x] Dashboard created
- [x] Business insights ready
- [x] Code tested
- [x] Documentation written

---

**Made by:** Lakshya Agarwal  
**Last Updated:** July 2026  
**Status:** ✅ Ready to submit
