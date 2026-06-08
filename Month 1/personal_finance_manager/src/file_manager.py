"""
file_manager.py - CSV read/write operations and data persistence
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery
"""

import csv
import os
import shutil
from datetime import datetime
from src.expense import Expense

DATA_FILE = "data/expenses.csv"
BACKUP_DIR = "data/backups"
FIELDNAMES = ["Date", "Category", "Amount", "Description"]


def ensure_directories():
    """Ensure required directories exist."""
    os.makedirs("data", exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    os.makedirs("reports", exist_ok=True)


def load_expenses(filename=DATA_FILE):
    """
    Load all expenses from CSV file.

    Args:
        filename (str): Path to the CSV data file.

    Returns:
        list: List of Expense objects.
    """
    expenses = []
    ensure_directories()

    if not os.path.exists(filename):
        return expenses

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    exp = Expense(
                        amount=row["Amount"],
                        category=row["Category"],
                        date=row["Date"],
                        description=row["Description"]
                    )
                    expenses.append(exp)
                except (ValueError, KeyError) as e:
                    print(f"  ⚠️  Skipping invalid row: {e}")
    except Exception as e:
        print(f"  ❌ Error loading data: {e}")

    return expenses


def save_expenses(expenses, filename=DATA_FILE):
    """
    Save all expenses to CSV file.

    Args:
        expenses (list): List of Expense objects to save.
        filename (str): Path to the CSV data file.

    Returns:
        bool: True if saved successfully, False otherwise.
    """
    ensure_directories()
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())
        return True
    except Exception as e:
        print(f"  ❌ Error saving data: {e}")
        return False


def backup_data(filename=DATA_FILE):
    """
    Create a timestamped backup of the expense data file.

    Returns:
        str: Path to the backup file, or None if backup failed.
    """
    ensure_directories()
    if not os.path.exists(filename):
        print("  ⚠️  No data file found to backup.")
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(BACKUP_DIR, f"expenses_backup_{timestamp}.csv")

    try:
        shutil.copy2(filename, backup_filename)
        print(f"  ✅ Backup created: {backup_filename}")
        return backup_filename
    except Exception as e:
        print(f"  ❌ Backup failed: {e}")
        return None


def restore_data(backup_filename, filename=DATA_FILE):
    """
    Restore expense data from a backup file.

    Args:
        backup_filename (str): Path to the backup file.
        filename (str): Path to restore to.

    Returns:
        bool: True if restored successfully.
    """
    if not os.path.exists(backup_filename):
        print(f"  ❌ Backup file not found: {backup_filename}")
        return False
    try:
        shutil.copy2(backup_filename, filename)
        print(f"  ✅ Data restored from: {backup_filename}")
        return True
    except Exception as e:
        print(f"  ❌ Restore failed: {e}")
        return False


def list_backups():
    """List all available backup files."""
    ensure_directories()
    backups = [f for f in os.listdir(BACKUP_DIR) if f.endswith(".csv")]
    backups.sort(reverse=True)
    return backups


def export_to_csv(expenses, filename):
    """Export a filtered list of expenses to a specific CSV file."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())
        return True
    except Exception as e:
        print(f"  ❌ Export failed: {e}")
        return False
