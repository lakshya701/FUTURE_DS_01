"""Utility functions for data analysis"""

import json
from pathlib import Path


def format_currency(value):
    """Format number as Indian currency (₹)"""
    if value >= 1_000_000:
        return f"₹{value/1_000_000:.1f}Cr"
    elif value >= 1_000:
        return f"₹{value/1_000:.1f}K"
    return f"₹{value:.0f}"


def format_percentage(value, decimals=2):
    """Format number as percentage"""
    return f"{value:.{decimals}f}%"


def save_json(data, filepath):
    """Save data to JSON file with pretty formatting"""
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def load_json(filepath):
    """Load data from JSON file"""
    with open(filepath, 'r') as f:
        return json.load(f)
