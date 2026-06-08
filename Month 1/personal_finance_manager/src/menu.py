"""
menu.py - Command-line interface and menu system
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery
"""

import os
from datetime import datetime
from src.expense import Expense
from src.utils import (
    format_currency, get_current_date, print_separator,
    print_header, validate_date_input, validate_amount_input, get_month_name
)
from src.file_manager import save_expenses, backup_data, list_backups, restore_data
from src.reports import (
    print_category_report, print_monthly_report,
    print_full_summary, export_monthly_report, get_monthly_summary
)


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def press_enter():
    """Wait for user to press Enter."""
    input("\n  Press Enter to continue...")


def print_banner():
    """Print the application banner."""
    clear_screen()
    print("=" * 50)
    print("       PERSONAL FINANCE MANAGER")
    print("       The Developers Arena | Month 1")
    print("=" * 50)
    print()


def print_main_menu():
    """Print the main menu."""
    print_banner()
    print("  MAIN MENU:")
    print()
    print("  1. Add New Expense")
    print("  2. View All Expenses")
    print("  3. View Category-wise Summary")
    print("  4. Generate Monthly Report")
    print("  5. Search Expenses")
    print("  6. Delete an Expense")
    print("  7. Backup Data")
    print("  8. Restore Data")
    print("  9. Export Monthly Report to CSV")
    print(" 10. Overall Summary")
    print("  0. Exit")
    print()
    print_separator()


def add_expense_ui(expenses):
    """UI for adding a new expense."""
    print_header("ADD NEW EXPENSE")

    try:
        # Amount
        amount_str = input("  Enter amount (₹): ").strip()
        amount = validate_amount_input(amount_str)

        # Category
        print(f"  Categories: {', '.join(Expense.VALID_CATEGORIES)}")
        category = input("  Enter category: ").strip().title()
        if not category:
            category = "Other"

        # Date
        default_date = get_current_date()
        date_str = input(f"  Enter date (YYYY-MM-DD) [default: {default_date}]: ").strip()
        if not date_str:
            date_str = default_date
        date = validate_date_input(date_str)

        # Description
        description = input("  Enter description: ").strip()
        if not description:
            description = "No description"

        # Create and save
        expense = Expense(amount=amount, category=category, date=date, description=description)
        expenses.append(expense)
        save_expenses(expenses)

        print()
        print(f"  ✅ Expense added successfully!")
        print(f"  📝 {expense}")

    except ValueError as e:
        print(f"\n  ❌ Error: {e}")

    press_enter()
    return expenses


def view_all_expenses_ui(expenses):
    """UI for viewing all expenses with pagination."""
    print_header("ALL EXPENSES")

    if not expenses:
        print("  No expenses recorded yet.")
        press_enter()
        return

    sorted_expenses = sorted(expenses, key=lambda e: e.date, reverse=True)
    page_size = 15
    total_pages = (len(sorted_expenses) + page_size - 1) // page_size
    current_page = 0

    while True:
        clear_screen()
        print_header(f"ALL EXPENSES  (Page {current_page + 1}/{total_pages})")
        print(f"  {'#':<5} {'Date':<12} {'Category':<16} {'Amount':>10}  Description")
        print_separator("-", 65)

        start = current_page * page_size
        end = start + page_size
        page_items = sorted_expenses[start:end]

        for i, exp in enumerate(page_items, start + 1):
            desc = exp.description[:22] + "..." if len(exp.description) > 22 else exp.description
            print(f"  {i:<5} {exp.date:<12} {exp.category:<16} {format_currency(exp.amount):>10}  {desc}")

        print_separator("-", 65)
        total = sum(e.amount for e in expenses)
        print(f"  Total Records: {len(expenses)}  |  Grand Total: {format_currency(total)}")
        print()
        print("  [N] Next Page  [P] Previous Page  [Q] Back to Menu")
        choice = input("  Your choice: ").strip().upper()

        if choice == "N" and current_page < total_pages - 1:
            current_page += 1
        elif choice == "P" and current_page > 0:
            current_page -= 1
        elif choice == "Q":
            break


def search_expenses_ui(expenses):
    """UI for searching expenses."""
    print_header("SEARCH EXPENSES")

    if not expenses:
        print("  No expenses to search.")
        press_enter()
        return

    print("  Search by:")
    print("  1. Category")
    print("  2. Date range")
    print("  3. Keyword in description")
    print("  4. Amount range")
    print()
    choice = input("  Enter choice (1-4): ").strip()

    results = []

    if choice == "1":
        print(f"  Categories: {', '.join(Expense.VALID_CATEGORIES)}")
        cat = input("  Enter category: ").strip().title()
        results = [e for e in expenses if e.category.lower() == cat.lower()]

    elif choice == "2":
        from_date = input("  From date (YYYY-MM-DD): ").strip()
        to_date = input("  To date   (YYYY-MM-DD): ").strip()
        try:
            validate_date_input(from_date)
            validate_date_input(to_date)
            results = [e for e in expenses if from_date <= e.date <= to_date]
        except ValueError as err:
            print(f"  ❌ {err}")
            press_enter()
            return

    elif choice == "3":
        keyword = input("  Enter keyword: ").strip().lower()
        results = [e for e in expenses if keyword in e.description.lower()]

    elif choice == "4":
        try:
            min_amt = float(input("  Minimum amount (₹): ").strip())
            max_amt = float(input("  Maximum amount (₹): ").strip())
            results = [e for e in expenses if min_amt <= e.amount <= max_amt]
        except ValueError:
            print("  ❌ Invalid amount entered.")
            press_enter()
            return
    else:
        print("  ❌ Invalid choice.")
        press_enter()
        return

    print()
    if not results:
        print("  No matching expenses found.")
    else:
        print(f"  Found {len(results)} result(s):\n")
        print(f"  {'#':<5} {'Date':<12} {'Category':<16} {'Amount':>10}  Description")
        print_separator("-", 65)
        for i, exp in enumerate(results, 1):
            desc = exp.description[:22] + "..." if len(exp.description) > 22 else exp.description
            print(f"  {i:<5} {exp.date:<12} {exp.category:<16} {format_currency(exp.amount):>10}  {desc}")
        print_separator("-", 65)
        print(f"  Total: {format_currency(sum(e.amount for e in results))}")

    press_enter()


def delete_expense_ui(expenses):
    """UI for deleting an expense."""
    print_header("DELETE AN EXPENSE")

    if not expenses:
        print("  No expenses to delete.")
        press_enter()
        return

    sorted_expenses = sorted(expenses, key=lambda e: e.date, reverse=True)

    print(f"  {'#':<5} {'Date':<12} {'Category':<16} {'Amount':>10}  Description")
    print_separator("-", 65)
    for i, exp in enumerate(sorted_expenses, 1):
        desc = exp.description[:22] + "..." if len(exp.description) > 22 else exp.description
        print(f"  {i:<5} {exp.date:<12} {exp.category:<16} {format_currency(exp.amount):>10}  {desc}")
    print()

    try:
        num = int(input("  Enter the # to delete (0 to cancel): ").strip())
        if num == 0:
            return
        if 1 <= num <= len(sorted_expenses):
            exp_to_del = sorted_expenses[num - 1]
            confirm = input(f"  Delete '{exp_to_del}'? (yes/no): ").strip().lower()
            if confirm in ("yes", "y"):
                expenses.remove(exp_to_del)
                save_expenses(expenses)
                print("  ✅ Expense deleted successfully.")
            else:
                print("  ❌ Deletion cancelled.")
        else:
            print("  ❌ Invalid number.")
    except ValueError:
        print("  ❌ Please enter a valid number.")

    press_enter()
    return expenses


def monthly_report_ui(expenses):
    """UI to select and display a monthly report."""
    print_header("MONTHLY REPORT")

    monthly = get_monthly_summary(expenses)
    if not monthly:
        print("  No data available.")
        press_enter()
        return

    keys = list(monthly.keys())
    print("  Available months:")
    for i, (yr, mo) in enumerate(keys, 1):
        count = len(monthly[(yr, mo)])
        total = sum(e.amount for e in monthly[(yr, mo)])
        print(f"  {i}. {get_month_name(mo)} {yr}  ({count} entries, {format_currency(total)})")
    print()

    try:
        choice = int(input("  Select month number (0 for all): ").strip())
        if choice == 0:
            print_monthly_report(expenses)
        elif 1 <= choice <= len(keys):
            yr, mo = keys[choice - 1]
            print_monthly_report(expenses, year=yr, month=mo)
        else:
            print("  ❌ Invalid choice.")
    except ValueError:
        print("  ❌ Invalid input.")

    press_enter()


def backup_ui():
    """UI for creating a data backup."""
    print_header("BACKUP DATA")
    backup_data()
    press_enter()


def restore_ui(expenses):
    """UI for restoring from backup."""
    print_header("RESTORE DATA")

    backups = list_backups()
    if not backups:
        print("  No backups found.")
        press_enter()
        return

    print("  Available backups:")
    for i, b in enumerate(backups, 1):
        print(f"  {i}. {b}")
    print()

    try:
        choice = int(input("  Select backup number to restore (0 to cancel): ").strip())
        if choice == 0:
            return
        if 1 <= choice <= len(backups):
            backup_path = os.path.join("data/backups", backups[choice - 1])
            confirm = input(f"  This will overwrite current data. Proceed? (yes/no): ").strip().lower()
            if confirm in ("yes", "y"):
                restore_data(backup_path)
        else:
            print("  ❌ Invalid selection.")
    except ValueError:
        print("  ❌ Invalid input.")

    press_enter()
    return expenses


def export_report_ui(expenses):
    """UI for exporting monthly report to CSV."""
    print_header("EXPORT MONTHLY REPORT")

    monthly = get_monthly_summary(expenses)
    if not monthly:
        print("  No data to export.")
        press_enter()
        return

    keys = list(monthly.keys())
    for i, (yr, mo) in enumerate(keys, 1):
        print(f"  {i}. {get_month_name(mo)} {yr}")
    print()

    try:
        choice = int(input("  Select month to export (0 to cancel): ").strip())
        if choice == 0:
            return
        if 1 <= choice <= len(keys):
            yr, mo = keys[choice - 1]
            export_monthly_report(expenses, yr, mo)
        else:
            print("  ❌ Invalid choice.")
    except ValueError:
        print("  ❌ Invalid input.")

    press_enter()
