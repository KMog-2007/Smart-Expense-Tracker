from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)
        return amount > 0
    except (ValueError, TypeError):
        return False


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def format_amount(amount):
    return f"₹{float(amount):.2f}"
