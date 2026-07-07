"""Unit tests for analysis module"""

import unittest
import pandas as pd
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.analysis import calculate_kpis, calculate_category_performance


class TestAnalysis(unittest.TestCase):
    """Test analysis functions"""
    
    def setUp(self):
        """Create sample data for testing"""
        self.df = pd.DataFrame({
            'Order ID': ['ORD001', 'ORD002', 'ORD003'],
            'Sales': [10000, 20000, 15000],
            'Profit': [2000, 4000, 3000],
            'Product Category': ['Tech', 'Tech', 'Furniture'],
            'Order Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03'])
        })
    
    def test_kpi_calculation(self):
        """Test KPI calculation"""
        kpis = calculate_kpis(self.df)
        self.assertEqual(kpis['revenue'], 45000)
        self.assertEqual(kpis['profit'], 9000)
        self.assertEqual(kpis['orders'], 3)
    
    def test_margin_calculation(self):
        """Test profit margin calculation"""
        kpis = calculate_kpis(self.df)
        expected_margin = (9000 / 45000) * 100
        self.assertAlmostEqual(kpis['margin'], round(expected_margin, 2))


if __name__ == '__main__':
    unittest.main()
