"""
test_expense.py - Unit tests for the Personal Finance Manager
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.expense import Expense
from src.utils import validate_amount_input, validate_date_input, format_currency
from src.reports import get_category_summary, calculate_statistics


class TestExpenseClass(unittest.TestCase):
    """Tests for the Expense class."""

    def test_valid_expense_creation(self):
        exp = Expense(1500.00, "Food", "2024-01-15", "Grocery shopping")
        self.assertEqual(exp.amount, 1500.00)
        self.assertEqual(exp.category, "Food")
        self.assertEqual(exp.date, "2024-01-15")
        self.assertEqual(exp.description, "Grocery shopping")

    def test_amount_rounding(self):
        exp = Expense(99.999, "Food", "2024-01-01", "Test")
        self.assertEqual(exp.amount, 100.00)

    def test_invalid_amount_zero(self):
        with self.assertRaises(ValueError):
            Expense(0, "Food", "2024-01-01", "Test")

    def test_invalid_amount_negative(self):
        with self.assertRaises(ValueError):
            Expense(-100, "Food", "2024-01-01", "Test")

    def test_invalid_amount_string(self):
        with self.assertRaises(ValueError):
            Expense("abc", "Food", "2024-01-01", "Test")

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            Expense(100, "Food", "15-01-2024", "Test")

    def test_invalid_date_string(self):
        with self.assertRaises(ValueError):
            Expense(100, "Food", "not-a-date", "Test")

    def test_to_dict(self):
        exp = Expense(500.0, "Transport", "2024-03-01", "Auto ride")
        d = exp.to_dict()
        self.assertEqual(d["Amount"], 500.0)
        self.assertEqual(d["Category"], "Transport")
        self.assertEqual(d["Date"], "2024-03-01")
        self.assertEqual(d["Description"], "Auto ride")

    def test_str_representation(self):
        exp = Expense(200.0, "Food", "2024-01-10", "Lunch")
        result = str(exp)
        self.assertIn("2024-01-10", result)
        self.assertIn("Food", result)
        self.assertIn("200.00", result)


class TestUtils(unittest.TestCase):
    """Tests for utility functions."""

    def test_validate_amount_valid(self):
        self.assertEqual(validate_amount_input("250"), 250.0)
        self.assertEqual(validate_amount_input("1500.50"), 1500.50)

    def test_validate_amount_invalid(self):
        with self.assertRaises(ValueError):
            validate_amount_input("abc")
        with self.assertRaises(ValueError):
            validate_amount_input("-100")
        with self.assertRaises(ValueError):
            validate_amount_input("0")

    def test_validate_date_valid(self):
        self.assertEqual(validate_date_input("2024-01-15"), "2024-01-15")

    def test_validate_date_invalid(self):
        with self.assertRaises(ValueError):
            validate_date_input("2024/01/15")
        with self.assertRaises(ValueError):
            validate_date_input("15-Jan-2024")

    def test_format_currency(self):
        self.assertEqual(format_currency(1000), "₹1,000.00")
        self.assertEqual(format_currency(0), "₹0.00")


class TestReports(unittest.TestCase):
    """Tests for report generation functions."""

    def setUp(self):
        self.expenses = [
            Expense(500.0, "Food", "2024-01-01", "Grocery"),
            Expense(300.0, "Food", "2024-01-05", "Restaurant"),
            Expense(200.0, "Transport", "2024-01-03", "Auto"),
            Expense(1000.0, "Shopping", "2024-01-10", "Clothes"),
        ]

    def test_category_summary(self):
        summary = get_category_summary(self.expenses)
        self.assertEqual(summary["Food"], 800.0)
        self.assertEqual(summary["Transport"], 200.0)
        self.assertEqual(summary["Shopping"], 1000.0)

    def test_calculate_statistics(self):
        stats = calculate_statistics(self.expenses)
        self.assertEqual(stats["total"], 2000.0)
        self.assertEqual(stats["count"], 4)
        self.assertEqual(stats["average"], 500.0)
        self.assertEqual(stats["max"].amount, 1000.0)
        self.assertEqual(stats["min"].amount, 200.0)

    def test_statistics_empty(self):
        stats = calculate_statistics([])
        self.assertEqual(stats, {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
