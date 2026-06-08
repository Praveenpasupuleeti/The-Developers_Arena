# 📘 User Guide — Personal Finance Manager

**The Developers Arena Internship | Month 1: Python Programming Mastery**

---

## 1. Introduction

The Personal Finance Manager is a Python command-line application designed to help you record, track, and analyze your daily expenses. It uses CSV files for data storage, making data easy to view and backup.

---

## 2. Installation Guide

### System Requirements
- Operating System: Windows 10/11, macOS, or Linux
- Python: Version 3.8 or higher
- Disk Space: ~5 MB

### Step-by-Step Installation

**Step 1 — Install Python**

Download from: https://www.python.org/downloads/

Verify installation:
```bash
python --version
```

**Step 2 — Download / Clone the Project**

```bash
git clone https://github.com/YOUR_USERNAME/personal_finance_manager.git
cd personal_finance_manager
```

**Step 3 — Run the Application**

```bash
python main.py
```

No additional package installation is required. The application uses only Python's built-in standard library.

---

## 3. Application Features

### 3.1 Add New Expense

Navigate to **Option 1** from the main menu.

You will be prompted to enter:

| Field | Format | Example |
|---|---|---|
| Amount | Positive number | `1500` or `250.50` |
| Category | From the list | `Food` |
| Date | YYYY-MM-DD | `2024-03-15` |
| Description | Free text | `Monthly grocery shopping` |

**Valid Categories:**
- Food
- Transport
- Entertainment
- Shopping
- Health
- Education
- Utilities
- Other

**Notes:**
- Press **Enter** on the date prompt to use today's date
- The app validates all inputs and shows clear error messages for invalid entries
- Data is saved immediately after adding

---

### 3.2 View All Expenses

Navigate to **Option 2**.

- Expenses are displayed sorted by date (newest first)
- Use **N** (Next) and **P** (Previous) to navigate pages (15 per page)
- Grand total is shown at the bottom
- Press **Q** to return to the main menu

---

### 3.3 View Category-wise Summary

Navigate to **Option 3**.

Shows a visual breakdown:
- Total amount per category
- Percentage of total spending
- ASCII bar chart for quick visual comparison

---

### 3.4 Generate Monthly Report

Navigate to **Option 4**.

- Lists all months that have data
- Select a month by number to view:
  - Total, average, highest and lowest expenses
  - Full list of entries for that month
  - Category breakdown for that month

---

### 3.5 Search Expenses

Navigate to **Option 5**.

Four search modes:

1. **By Category** — Shows all expenses in a chosen category
2. **By Date Range** — Enter from/to dates to filter
3. **By Keyword** — Searches description text
4. **By Amount Range** — Enter minimum and maximum amount

Results show matching entries with a subtotal.

---

### 3.6 Delete an Expense

Navigate to **Option 6**.

- All expenses are listed with numbers
- Enter the number of the entry to delete
- Confirm deletion when prompted (`yes` or `no`)
- Data file is updated immediately

---

### 3.7 Backup Data

Navigate to **Option 7**.

- Creates a timestamped copy of your data file
- Backups are saved to `data/backups/`
- Example backup name: `expenses_backup_20240315_142530.csv`
- Recommended to backup before making bulk changes

---

### 3.8 Restore Data

Navigate to **Option 8**.

- Lists all available backup files (newest first)
- Select a backup to restore from
- **Warning:** This overwrites current data
- Confirm before proceeding

---

### 3.9 Export Monthly Report to CSV

Navigate to **Option 9**.

- Select a month
- Exports all entries for that month to `reports/report_YYYY_MM.csv`
- Can be opened in Excel or Google Sheets

---

### 3.10 Overall Summary

Navigate to **Option 10**.

Shows across all recorded data:
- Total amount spent
- Number of entries
- Average expense
- Most and least expensive entries
- Number of months tracked
- Full category breakdown

---

## 4. Data Storage

### Main Data File
Location: `data/expenses.csv`

Format:
```
Date,Category,Amount,Description
2024-01-15,Food,1500.00,Grocery shopping
2024-01-20,Transport,200.00,Metro pass
```

### Backup Files
Location: `data/backups/expenses_backup_YYYYMMDD_HHMMSS.csv`

### Exported Reports
Location: `reports/report_YYYY_MM.csv`

---

## 5. Error Handling

The application handles the following errors gracefully:

| Error Type | Behaviour |
|---|---|
| Invalid amount (negative, zero, text) | Shows error message, prompts again |
| Invalid date format | Shows correct format, prompts again |
| Missing data file | Creates new empty storage |
| Corrupt CSV row | Skips row with warning, loads rest |
| Invalid menu choice | Shows error, re-displays menu |
| Empty description | Defaults to "No description" |

---

## 6. Troubleshooting

**Issue: "python not found"**
- Make sure Python is installed and added to PATH
- Try `python3 main.py` instead

**Issue: App shows garbled characters (₹ symbol)**
- Your terminal may not support UTF-8
- On Windows: Run `chcp 65001` before launching the app

**Issue: Data not saving**
- Make sure you have write permissions in the project folder
- Check if `data/` folder exists (it is auto-created)

**Issue: Tests failing**
- Make sure you run from the project root directory:
  ```bash
  python -m unittest tests/test_expense.py -v
  ```

---

## 7. Code Explanation

### Object-Oriented Design

The `Expense` class encapsulates all data and validation for a single expense entry. This means:
- Validation runs automatically when an Expense is created
- The object can serialize itself to a dictionary (`to_dict()`) for CSV storage
- Clean `__str__` representation for display

### Modular Architecture

Each module has a single responsibility:
- `expense.py` — data model only
- `file_manager.py` — I/O operations only
- `reports.py` — analysis and display only
- `menu.py` — user interaction only
- `utils.py` — shared helpers only
- `main.py` — application loop only

This separation makes the code easy to maintain, test, and extend.

### Data Persistence

The `csv` module (Python standard library) is used for reading and writing. When the app starts, `load_expenses()` reads the CSV and converts each row into an `Expense` object. When data changes, `save_expenses()` rewrites the entire file.

### Error Handling Strategy

Every user input is passed through a validation function in `utils.py` before being used. All file operations are wrapped in `try/except` blocks to handle missing files, permission errors, and corrupt data gracefully.

---

## 8. Testing

The test file `tests/test_expense.py` contains 17 unit tests using Python's built-in `unittest` framework.

Run all tests:
```bash
python -m unittest tests/test_expense.py -v
```

Test categories:
- **Expense creation** — valid inputs, edge cases
- **Validation** — invalid amounts, dates, formats
- **Serialization** — `to_dict()` correctness
- **Report logic** — category summary, statistics calculation
- **Utility functions** — currency formatting, input validation

All 17 tests pass successfully.

---

*Documentation prepared for The Developers Arena Internship — Month 1 Submission*
