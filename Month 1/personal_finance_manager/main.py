"""
main.py - Main program entry point
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery

Author: Intern
Organization: The Developers Arena
"""

import sys
import os

# Ensure the project root is on the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.file_manager import load_expenses, ensure_directories
from src.reports import print_full_summary
from src.menu import (
    print_main_menu,
    add_expense_ui,
    view_all_expenses_ui,
    search_expenses_ui,
    delete_expense_ui,
    monthly_report_ui,
    backup_ui,
    restore_ui,
    export_report_ui,
    print_category_report,
    press_enter,
    clear_screen,
)


def main():
    """Main application loop."""
    ensure_directories()
    expenses = load_expenses()

    print(f"\n  ✅ Loaded {len(expenses)} expense(s) from data file.\n")

    while True:
        print_main_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            expenses = add_expense_ui(expenses)

        elif choice == "2":
            view_all_expenses_ui(expenses)

        elif choice == "3":
            clear_screen()
            print_category_report(expenses)
            press_enter()

        elif choice == "4":
            monthly_report_ui(expenses)

        elif choice == "5":
            search_expenses_ui(expenses)

        elif choice == "6":
            expenses = delete_expense_ui(expenses) or expenses

        elif choice == "7":
            backup_ui()

        elif choice == "8":
            restore_ui(expenses)
            expenses = load_expenses()  # Reload after restore

        elif choice == "9":
            export_report_ui(expenses)

        elif choice == "10":
            clear_screen()
            print_full_summary(expenses)
            press_enter()

        elif choice == "0":
            clear_screen()
            print("\n  👋 Thank you for using Personal Finance Manager!")
            print("  Goodbye!\n")
            sys.exit(0)

        else:
            print("\n  ❌ Invalid choice. Please enter a number from 0 to 10.")
            press_enter()


if __name__ == "__main__":
    main()
