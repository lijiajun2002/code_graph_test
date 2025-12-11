"""
Utility functions.
"""

def validate_number(value):
    """Validate if value is a number."""
    return isinstance(value, (int, float))

def format_result(result):
    """Format calculation result with prefix."""
    return f"Calculation Result: {result:.2f}"

def round_result(result, decimals=2):
    """Round result to specified decimal places."""
    return round(result, decimals)

def is_positive(value):
    """Check if value is positive."""
    return value > 0
