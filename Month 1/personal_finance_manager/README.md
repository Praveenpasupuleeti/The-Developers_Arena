# 💰 Personal Finance Manager

> **The Developers Arena Internship | Month 1: Python Programming Mastery**

A comprehensive command-line personal finance management system built with Python. Track expenses, generate reports, analyze spending patterns, and manage your financial data — all from your terminal.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Usage Guide](#usage-guide)
- [Sample Output](#sample-output)
- [Code Architecture](#code-architecture)
- [Testing](#testing)
- [Technologies Used](#technologies-used)

---

## 🎯 Project Overview

The **Personal Finance Manager** is a fully object-oriented Python application that allows users to:

- Record and manage daily expenses across multiple categories
- Persist data using CSV file storage
- Generate detailed monthly and category-wise reports
- Search and filter expenses by various criteria
- Backup and restore expense data
- Export reports to CSV files

This project demonstrates core Python concepts including:
- Object-Oriented Programming (OOP)
- File handling with the `csv` module
- Error handling and input validation
- Modular code organization
- Command-line interface design

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Expense | Record expenses with amount, category, date, description |
| 📋 View All | Paginated view of all expenses sorted by date |
| 📊 Category Report | Visual bar chart of spending by category |
| 📅 Monthly Report | Detailed month-by-month breakdown with statistics |
| 🔍 Search | Filter by category, date range, keyword, or amount |
| 🗑️ Delete | Remove incorrect or duplicate entries |
| 💾 Backup | Create timestamped backups of your data |
| 🔄 Restore | Restore from any previous backup |
| 📤 Export | Export monthly reports to CSV |
| 📈 Summary | Overall financial statistics and trends |

---

## 📁 Project Structure

```
personal_finance_manager/
│
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── README.md                # This file
│
├── src/                     # Source code modules
│   ├── __init__.py
│   ├── expense.py           # Expense class definition
│   ├── file_manager.py      # CSV read/write & backup operations
│   ├── menu.py              # Command-line interface & menus
│   ├── reports.py           # Report generation & analytics
│   └── utils.py             # Utility functions & validators
│
├── data/                    # Data storage
│   ├── expenses.csv         # Main expense data file
│   └── backups/             # Auto-created backup files
│
├── reports/                 # Exported report files (auto-created)
│
├── docs/                    # Documentation
│   └── user_guide.md        # Detailed user guide
│
├── tests/                   # Unit tests
│   └── test_expense.py      # Tests for core functionality
│
└── screenshots/             # Application screenshots
```

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- No third-party packages required (uses Python standard library only)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/personal_finance_manager.git
cd personal_finance_manager
```

### Step 2: Verify Python Installation

```bash
python --version
# Should show Python 3.8+
```

### Step 3: (Optional) Create Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
# Note: No external packages are required for the basic version
```

---

## ▶️ How to Run

```bash
python main.py
```

To run with sample data already loaded:
```bash
# Sample data is in data/expenses.csv — just run:
python main.py
```

To run unit tests:
```bash
python -m unittest tests/test_expense.py -v
```

---

## 🖥️ Usage Guide

### Main Menu

```
==================================================
       PERSONAL FINANCE MANAGER
       The Developers Arena | Month 1
==================================================

  MAIN MENU:

  1. Add New Expense
  2. View All Expenses
  3. View Category-wise Summary
  4. Generate Monthly Report
  5. Search Expenses
  6. Delete an Expense
  7. Backup Data
  8. Restore Data
  9. Export Monthly Report to CSV
 10. Overall Summary
  0. Exit
```

### Adding an Expense

1. Select **Option 1** from the main menu
2. Enter the amount (e.g., `1500`)
3. Choose a category (Food / Transport / Entertainment / Shopping / Health / Education / Utilities / Other)
4. Enter date in `YYYY-MM-DD` format (press Enter for today's date)
5. Enter a short description

### Viewing Reports

- **Option 3**: See category-wise spending with a visual bar chart
- **Option 4**: Select a specific month and see detailed breakdown
- **Option 10**: View overall statistics across all recorded data

### Searching Expenses

- By **Category**: Filter all Food/Transport/etc. expenses
- By **Date Range**: View expenses between two dates
- By **Keyword**: Search description text
- By **Amount Range**: Find expenses between min and max values

---

## 📊 Sample Output

### Category Report
```
==================================================
  CATEGORY-WISE SPENDING REPORT
==================================================
  Category             Total            % Bar
------------------------------------------------------------
  Shopping         ₹7,500.00    30.6% ██████
  Food             ₹4,800.00    19.6% ███
  Education        ₹3,500.00    14.3% ██
  Health           ₹2,550.00    10.4% ██
  Utilities        ₹2,500.00    10.2% ██
  Entertainment    ₹1,997.00     8.2% █
  Transport        ₹1,650.00     6.7% █
------------------------------------------------------------
  TOTAL           ₹24,497.00
```

### Overall Summary
```
==================================================
  OVERALL FINANCIAL SUMMARY
==================================================
  Total Spent       : ₹24,497.00
  Total Entries     : 30
  Average per Entry : ₹816.57
  Most Expensive    : ₹3,500.00 - New clothes for summer
  Least Expensive   : ₹180.00 - Evening snacks
  Months Tracked    : 3
```

---

## 🏗️ Code Architecture

### `Expense` Class (`src/expense.py`)
The core data model. Each expense object contains:
- `amount` (float) — monetary value in INR
- `category` (str) — expense type
- `date` (str) — in YYYY-MM-DD format
- `description` (str) — short text note

Includes built-in validation for all fields and a `to_dict()` method for CSV serialization.

### `file_manager.py` (`src/file_manager.py`)
Handles all data persistence:
- `load_expenses()` — reads CSV and returns list of Expense objects
- `save_expenses()` — writes list of Expense objects to CSV
- `backup_data()` — creates a timestamped copy of the data file
- `restore_data()` — replaces current data from a backup

### `reports.py` (`src/reports.py`)
Analysis and reporting:
- `get_category_summary()` — totals per category
- `get_monthly_summary()` — groups expenses by month
- `calculate_statistics()` — computes total, avg, min, max
- `print_category_report()` — visual bar chart in terminal
- `print_monthly_report()` — detailed per-month breakdown

### `menu.py` (`src/menu.py`)
All user interaction logic — each menu item has a dedicated `_ui()` function.

### `utils.py` (`src/utils.py`)
Shared helper functions: input validation, currency formatting, date utilities, display helpers.

---

## 🧪 Testing

17 unit tests covering:
- Expense creation and validation
- Amount validation (zero, negative, non-numeric)
- Date format validation
- CSV serialization (`to_dict`)
- Category summary calculations
- Statistics calculations
- Utility function correctness

```bash
python -m unittest tests/test_expense.py -v
```

**Expected output:**
```
Ran 17 tests in 0.011s
OK
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core programming language |
| `csv` module | Data persistence and file I/O |
| `os` / `shutil` | File system operations and backups |
| `datetime` | Date parsing and validation |
| `collections.defaultdict` | Category and monthly grouping |
| `unittest` | Automated testing |

---

## 👤 Author

**Intern — The Developers Arena**
Month 1 Submission: Python Programming Mastery
December 2025 Batch

---

## 📄 License

This project was developed as part of The Developers Arena internship program.
