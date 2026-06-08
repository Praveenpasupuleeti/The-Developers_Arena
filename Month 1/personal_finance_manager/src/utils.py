"""
utils.py - Utility functions and validation helpers
Personal Finance Manager - The Developers Arena Internship
Month 1: Python Programming Mastery
"""

from datetime import datetime


def format_currency(amount):
    """Format a number as Indian Rupee currency string."""
    return f"₹{amount:,.2f}"


def get_current_date():
    """Return today's date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")


def get_current_month_year():
    """Return current month and year as (int, int)."""
    now = datetime.now()
    return now.month, now.year


def validate_date_input(date_str):
    """
    Validate date string in YYYY-MM-DD format.

    Returns:
        str: Valid date string or raises ValueError.
    """
    try:
        datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return date_str.strip()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format (e.g., 2024-01-15).")


def validate_amount_input(amount_str):
    """
    Validate monetary amount string.

    Returns:
        float: Valid positive float amount.
    """
    try:
        value = float(amount_str.strip())
        if value <= 0:
            raise ValueError("Amount must be greater than zero.")
        return round(value, 2)
    except ValueError:
        raise ValueError("Amount must be a positive number (e.g., 250 or 1500.50).")


def get_month_name(month_number):
    """Return month name from month number (1-12)."""
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    return "Unknown"


def print_separator(char="=", length=50):
    """Print a separator line."""
    print(char * length)


def print_header(title):
    """Print a formatted section header."""
    print_separator()
    print(f"  {title}")
    print_separator()


def paginate_list(items, page_size=10):
    """
    Split a list into pages.

    Returns:
        list of lists: Pages of items.
    """
    return [items[i:i + page_size] for i in range(0, len(items), page_size)]


def safe_input(prompt, input_type=str, allow_empty=False):
    """
    Safely get and validate input from user.

    Args:
        prompt (str): Input prompt.
        input_type (type): Expected type (str, float, int).
        allow_empty (bool): Allow empty string responses.

    Returns:
        Converted input value.
    """
    while True:
        try:
            raw = input(prompt).strip()
            if not raw and not allow_empty:
                print("  ⚠️  Input cannot be empty. Please try again.")
                continue
            if input_type == float:
                return float(raw)
            elif input_type == int:
                return int(raw)
            return raw
        except ValueError:
            print(f"  ⚠️  Invalid input. Expected a {input_type.__name__}. Please try again.")
