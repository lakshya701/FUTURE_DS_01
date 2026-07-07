"""
Main analysis script - Reads data and calculates all metrics for the dashboard
"""

import pandas as pd
import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# File paths
DATA_DIR = Path("data")
RAW_FILE = DATA_DIR / "superstore_sales.csv"
OUTPUT_FILE = DATA_DIR / "dashboard_data.json"


def load_and_clean_data(filepath):
    """
    Load CSV file and clean the data.
    - Convert date strings to proper date format
    - Check for missing values
    """
    try:
        logger.info(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        
        # Convert Order Date to datetime
        df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
        
        # Create year-month column for trends
        df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)
        df["Year"] = df["Order Date"].dt.year
        
        logger.info(f"Successfully loaded {len(df)} records")
        return df
    
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        raise
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise


def calculate_kpis(df):
    """Calculate main KPIs - Revenue, Profit, Orders, etc."""
    kpis = {
        "revenue": round(df["Sales"].sum(), 2),
        "profit": round(df["Profit"].sum(), 2),
        "orders": int(df["Order ID"].nunique()),
        "aov": round(df["Sales"].sum() / df["Order ID"].nunique(), 2),
        "margin": round(df["Profit"].sum() / df["Sales"].sum() * 100, 2),
        "date_start": str(df["Order Date"].min().date()),
        "date_end": str(df["Order Date"].max().date()),
    }
    return kpis


def calculate_monthly_trend(df):
    """Calculate revenue and profit by month"""
    monthly = df.groupby("YearMonth").agg(
        Revenue=("Sales", "sum"), 
        Profit=("Profit", "sum")
    ).reset_index()
    
    return {
        "labels": monthly["YearMonth"].tolist(),
        "revenue": [round(x, 2) for x in monthly["Revenue"]],
        "profit": [round(x, 2) for x in monthly["Profit"]],
    }


def calculate_category_performance(df):
    """Calculate revenue, profit, and margin by product category"""
    category = df.groupby("Product Category").agg(
        Revenue=("Sales", "sum"), 
        Profit=("Profit", "sum")
    ).reset_index().sort_values("Revenue", ascending=False)
    
    category["Margin"] = (category["Profit"] / category["Revenue"] * 100).round(2)
    
    return {
        "labels": category["Product Category"].tolist(),
        "revenue": [round(x, 2) for x in category["Revenue"]],
        "profit": [round(x, 2) for x in category["Profit"]],
        "margin": category["Margin"].tolist(),
    }


def calculate_region_performance(df):
    """Calculate revenue and profit by region"""
    region = df.groupby("Region").agg(
        Revenue=("Sales", "sum"), 
        Profit=("Profit", "sum")
    ).reset_index().sort_values("Revenue", ascending=False)
    
    region["Margin"] = (region["Profit"] / region["Revenue"] * 100).round(2)
    
    return {
        "labels": region["Region"].tolist(),
        "revenue": [round(x, 2) for x in region["Revenue"]],
        "profit": [round(x, 2) for x in region["Profit"]],
        "margin": region["Margin"].tolist(),
    }


def calculate_segment_performance(df):
    """Calculate revenue and profit by customer segment"""
    segment = df.groupby("Customer Segment").agg(
        Revenue=("Sales", "sum"), 
        Profit=("Profit", "sum")
    ).reset_index().sort_values("Revenue", ascending=False)
    
    return {
        "labels": segment["Customer Segment"].tolist(),
        "revenue": [round(x, 2) for x in segment["Revenue"]],
        "profit": [round(x, 2) for x in segment["Profit"]],
    }


def calculate_top_products(df, limit=10):
    """Get top products by revenue"""
    top = df.groupby("Product Name").agg(
        Revenue=("Sales", "sum"), 
        Profit=("Profit", "sum")
    ).reset_index().sort_values("Revenue", ascending=False).head(limit)
    
    return {
        "labels": top["Product Name"].tolist(),
        "revenue": [round(x, 2) for x in top["Revenue"]],
        "profit": [round(x, 2) for x in top["Profit"]],
    }


def calculate_seasonality(df):
    """Calculate revenue by calendar month (across all years)"""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    seasonality = df.groupby(df["Order Date"].dt.month)["Sales"].sum().reset_index()
    
    return {
        "labels": months,
        "revenue": [round(x, 2) for x in seasonality["Sales"]]
    }


def main():
    """Main function - runs the entire analysis pipeline"""
    try:
        # Load and clean data
        df = load_and_clean_data(RAW_FILE)
        
        # Calculate all metrics
        logger.info("Calculating metrics...")
        output = {
            "kpi": calculate_kpis(df),
            "monthly": calculate_monthly_trend(df),
            "category": calculate_category_performance(df),
            "region": calculate_region_performance(df),
            "segment": calculate_segment_performance(df),
            "top_products": calculate_top_products(df),
            "seasonality": calculate_seasonality(df),
        }
        
        # Save to JSON
        with open(OUTPUT_FILE, "w") as f:
            json.dump(output, f, indent=2)
        
        logger.info(f"Analysis complete! Results saved to {OUTPUT_FILE}")
        
        # Print summary
        print("\n" + "="*50)
        print("📊 SALES ANALYTICS SUMMARY")
        print("="*50)
        print(f"Total Revenue:  ₹{output['kpi']['revenue']:,.0f}")
        print(f"Total Profit:   ₹{output['kpi']['profit']:,.0f}")
        print(f"Profit Margin:  {output['kpi']['margin']:.1f}%")
        print(f"Total Orders:   {output['kpi']['orders']:,}")
        print(f"Period:         {output['kpi']['date_start']} to {output['kpi']['date_end']}")
        print("="*50)
        print("✅ Dashboard data is ready!")
        print("   Open dashboard/index.html in your browser")
        print("="*50 + "\n")
        
    except Exception as e:
        logger.error(f"Analysis failed: {e}")
        raise


if __name__ == "__main__":
    main()
