"""
Advanced mathematical operations.
"""
import math

def power(base, exponent):
    """Calculate base raised to exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Arguments must be numbers")
    return math.pow(base, exponent)

def square_root(value):
    """Calculate square root."""
    if not isinstance(value, (int, float)):
        raise TypeError("Argument must be a number")
    if value < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(value)

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
