"""
reports.py - Report generation and analysis functions
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery
"""

from collections import defaultdict
from datetime import datetime
from src.utils import format_currency, get_month_name, print_separator, print_header
from src.file_manager import export_to_csv
import os


def get_category_summary(expenses):
    """
    Calculate total spending per category.

    Args:
        expenses (list): List of Expense objects.

    Returns:
        dict: {category: total_amount}
    """
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount
    return dict(sorted(summary.items(), key=lambda x: x[1], reverse=True))


def get_monthly_summary(expenses):
    """
    Group expenses by month and year.

    Returns:
        dict: {(year, month): [expenses]}
    """
    monthly = defaultdict(list)
    for exp in expenses:
        try:
            dt = datetime.strptime(exp.date, "%Y-%m-%d")
            monthly[(dt.year, dt.month)].append(exp)
        except ValueError:
            pass
    return dict(sorted(monthly.items(), reverse=True))


def calculate_statistics(expenses):
    """
    Calculate key statistics from a list of expenses.

    Returns:
        dict: Statistics dictionary.
    """
    if not expenses:
        return {}

    amounts = [e.amount for e in expenses]
    total = sum(amounts)
    avg = total / len(amounts)
    max_exp = max(expenses, key=lambda e: e.amount)
    min_exp = min(expenses, key=lambda e: e.amount)

    return {
        "total": total,
        "count": len(expenses),
        "average": avg,
        "max": max_exp,
        "min": min_exp
    }


def print_category_report(expenses):
    """Print a formatted category-wise spending report."""
    print_header("CATEGORY-WISE SPENDING REPORT")

    if not expenses:
        print("  No expenses found.")
        return

    summary = get_category_summary(expenses)
    stats = calculate_statistics(expenses)
    total = stats.get("total", 0)

    print(f"  {'Category':<20} {'Total':>12} {'%':>8} {'Bar'}")
    print_separator("-", 60)

    for category, amount in summary.items():
        percent = (amount / total * 100) if total > 0 else 0
        bar = "█" * int(percent / 5)
        print(f"  {category:<20} {format_currency(amount):>12} {percent:>7.1f}% {bar}")

    print_separator("-", 60)
    print(f"  {'TOTAL':<20} {format_currency(total):>12}")
    print()


def print_monthly_report(expenses, year=None, month=None):
    """Print a formatted monthly expense report."""
    monthly_data = get_monthly_summary(expenses)

    if year and month:
        # Filter to specific month
        key = (year, month)
        if key not in monthly_data:
            print(f"  No expenses found for {get_month_name(month)} {year}.")
            return
        items = {key: monthly_data[key]}
    else:
        items = monthly_data

    for (yr, mo), exps in items.items():
        print_header(f"REPORT: {get_month_name(mo).upper()} {yr}")
        stats = calculate_statistics(exps)

        print(f"  Total Expenses  : {format_currency(stats['total'])}")
        print(f"  No. of Entries  : {stats['count']}")
        print(f"  Average Expense : {format_currency(stats['average'])}")
        print(f"  Highest Expense : {format_currency(stats['max'].amount)} ({stats['max'].description})")
        print(f"  Lowest Expense  : {format_currency(stats['min'].amount)} ({stats['min'].description})")
        print()

        print(f"  {'#':<4} {'Date':<12} {'Category':<16} {'Amount':>10}  Description")
        print_separator("-", 65)
        for i, exp in enumerate(exps, 1):
            desc = exp.description[:25] + "..." if len(exp.description) > 25 else exp.description
            print(f"  {i:<4} {exp.date:<12} {exp.category:<16} {format_currency(exp.amount):>10}  {desc}")
        print()

        # Category breakdown for the month
        cat_summary = get_category_summary(exps)
        print(f"  Category Breakdown:")
        for cat, amt in cat_summary.items():
            print(f"    • {cat:<18} {format_currency(amt)}")
        print()


def print_full_summary(expenses):
    """Print an overall summary of all expenses."""
    print_header("OVERALL FINANCIAL SUMMARY")

    if not expenses:
        print("  No expenses recorded yet.")
        return

    stats = calculate_statistics(expenses)
    monthly = get_monthly_summary(expenses)

    print(f"  Total Spent       : {format_currency(stats['total'])}")
    print(f"  Total Entries     : {stats['count']}")
    print(f"  Average per Entry : {format_currency(stats['average'])}")
    print(f"  Most Expensive    : {format_currency(stats['max'].amount)} - {stats['max'].description}")
    print(f"  Least Expensive   : {format_currency(stats['min'].amount)} - {stats['min'].description}")
    print(f"  Months Tracked    : {len(monthly)}")
    print()
    print_category_report(expenses)


def export_monthly_report(expenses, year, month):
    """Export a monthly report to a CSV file in the reports/ directory."""
    monthly = get_monthly_summary(expenses)
    key = (year, month)

    if key not in monthly:
        print(f"  ⚠️  No data for {get_month_name(month)} {year}.")
        return

    os.makedirs("reports", exist_ok=True)
    filename = f"reports/report_{year}_{month:02d}.csv"
    exps = monthly[key]

    if export_to_csv(exps, filename):
        print(f"  ✅ Report exported to: {filename}")
    else:
        print(f"  ❌ Failed to export report.")
