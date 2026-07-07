"""
Business Sales Performance Analytics
Future Interns - Data Science & Analytics, Task 1 (2026)

Dataset : Superstore Sales Dataset (2009-2012, 8,399 order lines)
Author  : Lakshya

This script cleans the raw sales data and produces every metric used in the
client-ready dashboard (dashboard.html) and the written report (README.md):
    - Revenue / profit KPIs and overall margin
    - Monthly & yearly revenue-profit trend
    - Category / sub-category performance (revenue, profit, margin)
    - Regional performance
    - Customer segment performance
    - Top 10 products by revenue
    - Seasonality (revenue by calendar month)
"""

import pandas as pd
import json

RAW_FILE = "superstore_clean.csv"   # cleaned CSV (line endings normalised to \n)
OUT_FILE = "dashboard_data.json"    # feeds the HTML dashboard


def load_and_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
    df["YearMonth"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Year"] = df["Order Date"].dt.year
    return df


def kpis(df: pd.DataFrame) -> dict:
    return {
        "revenue": round(df["Sales"].sum(), 2),
        "profit": round(df["Profit"].sum(), 2),
        "orders": int(df["Order ID"].nunique()),
        "aov": round(df["Sales"].sum() / df["Order ID"].nunique(), 2),
        "margin": round(df["Profit"].sum() / df["Sales"].sum() * 100, 2),
        "date_start": str(df["Order Date"].min().date()),
        "date_end": str(df["Order Date"].max().date()),
    }


def monthly_trend(df: pd.DataFrame) -> dict:
    m = df.groupby("YearMonth").agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum")).reset_index()
    return {
        "labels": m["YearMonth"].tolist(),
        "revenue": [round(x, 2) for x in m["Revenue"]],
        "profit": [round(x, 2) for x in m["Profit"]],
    }


def category_performance(df: pd.DataFrame) -> dict:
    c = (
        df.groupby("Product Category")
        .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
        .reset_index()
        .sort_values("Revenue", ascending=False)
    )
    c["Margin"] = (c["Profit"] / c["Revenue"] * 100).round(2)
    return {
        "labels": c["Product Category"].tolist(),
        "revenue": [round(x, 2) for x in c["Revenue"]],
        "profit": [round(x, 2) for x in c["Profit"]],
        "margin": c["Margin"].tolist(),
    }


def subcategory_performance(df: pd.DataFrame) -> dict:
    s = (
        df.groupby("Product Sub-Category")
        .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
        .reset_index()
        .sort_values("Revenue", ascending=False)
    )
    return {
        "labels": s["Product Sub-Category"].tolist(),
        "revenue": [round(x, 2) for x in s["Revenue"]],
        "profit": [round(x, 2) for x in s["Profit"]],
    }


def region_performance(df: pd.DataFrame) -> dict:
    r = (
        df.groupby("Region")
        .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
        .reset_index()
        .sort_values("Revenue", ascending=False)
    )
    r["Margin"] = (r["Profit"] / r["Revenue"] * 100).round(2)
    return {
        "labels": r["Region"].tolist(),
        "revenue": [round(x, 2) for x in r["Revenue"]],
        "profit": [round(x, 2) for x in r["Profit"]],
        "margin": r["Margin"].tolist(),
    }


def segment_performance(df: pd.DataFrame) -> dict:
    s = (
        df.groupby("Customer Segment")
        .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
        .reset_index()
        .sort_values("Revenue", ascending=False)
    )
    return {
        "labels": s["Customer Segment"].tolist(),
        "revenue": [round(x, 2) for x in s["Revenue"]],
        "profit": [round(x, 2) for x in s["Profit"]],
    }


def top_products(df: pd.DataFrame, n: int = 10) -> dict:
    p = (
        df.groupby("Product Name")
        .agg(Revenue=("Sales", "sum"), Profit=("Profit", "sum"))
        .reset_index()
        .sort_values("Revenue", ascending=False)
        .head(n)
    )
    return {
        "labels": p["Product Name"].tolist(),
        "revenue": [round(x, 2) for x in p["Revenue"]],
        "profit": [round(x, 2) for x in p["Profit"]],
    }


def seasonality(df: pd.DataFrame) -> dict:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    s = df.groupby(df["Order Date"].dt.month)["Sales"].sum().reset_index()
    return {"labels": months, "revenue": [round(x, 2) for x in s["Sales"]]}


def main():
    df = load_and_clean(RAW_FILE)

    output = {
        "kpi": kpis(df),
        "monthly": monthly_trend(df),
        "category": category_performance(df),
        "subcategory": subcategory_performance(df),
        "region": region_performance(df),
        "segment": segment_performance(df),
        "top_products": top_products(df),
        "seasonality": seasonality(df),
    }

    with open(OUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Analysis complete -> {OUT_FILE}")
    print(f"Total revenue : ${output['kpi']['revenue']:,.2f}")
    print(f"Total profit  : ${output['kpi']['profit']:,.2f}")
    print(f"Profit margin : {output['kpi']['margin']}%")


if __name__ == "__main__":
    main()
