"""
Utility functions.
"""

def validate_number(value):
    """Validate if value is a number."""
    return isinstance(value, (int, float))

def format_result(result):
    """Format calculation result."""
    return f"Result: {result}"
