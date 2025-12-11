"""
Advanced mathematical operations.
"""
import math

def power(base, exponent):
    """Calculate base raised to exponent."""
    return math.pow(base, exponent)

def square_root(value):
    """Calculate square root."""
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
