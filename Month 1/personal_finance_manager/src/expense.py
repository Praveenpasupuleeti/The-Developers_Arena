"""
expense.py - Expense class definition
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery
"""

from datetime import datetime


class Expense:
    """
    Represents a single financial expense entry.

    Attributes:
        amount (float): The monetary amount of the expense in INR.
        category (str): Category of the expense (e.g., Food, Transport).
        date (str): Date of the expense in YYYY-MM-DD format.
        description (str): Short description of the expense.
    """

    VALID_CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Health", "Education", "Utilities", "Other"]

    def __init__(self, amount, category, date, description):
        """Initialize an Expense object with validation."""
        self.amount = self._validate_amount(amount)
        self.category = self._validate_category(category)
        self.date = self._validate_date(date)
        self.description = str(description).strip()

    def _validate_amount(self, amount):
        """Validate and return float amount."""
        try:
            value = float(amount)
            if value <= 0:
                raise ValueError("Amount must be greater than zero.")
            return round(value, 2)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid amount: '{amount}'. Please enter a positive number.")

    def _validate_category(self, category):
        """Validate and return category string."""
        cat = str(category).strip().title()
        if cat not in self.VALID_CATEGORIES:
            # Accept it but normalize to 'Other' if totally unknown
            return cat
        return cat

    def _validate_date(self, date):
        """Validate date format YYYY-MM-DD."""
        try:
            datetime.strptime(str(date), "%Y-%m-%d")
            return str(date)
        except ValueError:
            raise ValueError(f"Invalid date: '{date}'. Use YYYY-MM-DD format (e.g., 2024-01-15).")

    def to_dict(self):
        """Convert Expense to dictionary for CSV storage."""
        return {
            "Date": self.date,
            "Category": self.category,
            "Amount": self.amount,
            "Description": self.description
        }

    def __str__(self):
        return f"{self.date} | {self.category:<15} | ₹{self.amount:>10.2f} | {self.description}"

    def __repr__(self):
        return f"Expense(amount={self.amount}, category='{self.category}', date='{self.date}', description='{self.description}')"
