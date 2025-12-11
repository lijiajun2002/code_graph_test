"""
Calculator module with basic arithmetic operations.
Version: 1.0
"""
from git_operation.utils import validate_number

def add(a, b):
    """Add two numbers together."""
    if not validate_number(a) or not validate_number(b):
        raise TypeError("Both arguments must be numbers")
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    if not validate_number(a) or not validate_number(b):
        raise TypeError("Both arguments must be numbers")
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    if not validate_number(a) or not validate_number(b):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """Divide a by b."""
    if not validate_number(a) or not validate_number(b):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
