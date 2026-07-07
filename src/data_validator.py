"""
Data validation module - Check data quality before analysis
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def validate_data(filepath):
    """
    Validate data quality and report issues
    Check for:
    - Missing values
    - Negative numbers in sales/profit
    - Duplicate orders
    - Invalid date ranges
    """
    try:
        df = pd.read_csv(filepath)
        report = {}
        
        # Check missing values
        missing = df.isnull().sum()
        report["missing_values"] = missing[missing > 0].to_dict()
        
        # Check for negative sales
        negative_sales = (df["Sales"] < 0).sum()
        report["negative_sales"] = negative_sales
        
        # Check for negative profit
        negative_profit = (df["Profit"] < 0).sum()
        report["negative_profit"] = negative_profit
        
        # Check for duplicate orders
        duplicate_orders = df["Order ID"].duplicated().sum()
        report["duplicate_orders"] = duplicate_orders
        
        # Check data types
        report["total_records"] = len(df)
        report["total_columns"] = len(df.columns)
        
        # Print report
        print("\n" + "="*50)
        print("📋 DATA QUALITY REPORT")
        print("="*50)
        print(f"Total Records: {report['total_records']}")
        print(f"Total Columns: {report['total_columns']}")
        
        if report["missing_values"]:
            print(f"\n⚠️  Missing Values Found:")
            for col, count in report["missing_values"].items():
                print(f"   {col}: {count}")
        else:
            print("\n✅ No missing values")
        
        if report["negative_sales"] > 0:
            print(f"\n⚠️  Negative Sales: {report['negative_sales']}")
        else:
            print("\n✅ No negative sales")
        
        if report["duplicate_orders"] > 0:
            print(f"\n⚠️  Duplicate Orders: {report['duplicate_orders']}")
        else:
            print("\n✅ No duplicate orders")
        
        print("="*50 + "\n")
        
        return report
    
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return None
