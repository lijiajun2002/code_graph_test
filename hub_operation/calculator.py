"""
Calculator Module

Basic calculator with four fundamental operations.
This module is part of the code_graph_test project for testing GitHub collaboration features.
"""


class CalculatorError(Exception):
    """Base exception for calculator errors"""
    pass


class InvalidInputError(CalculatorError):
    """Raised when input is not a valid number"""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero"""
    pass


class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def _validate_input(self, *args):
        """
        Validate that all inputs are numeric.
        
        Args:
            *args: Values to validate
            
        Raises:
            InvalidInputError: If any input is not numeric
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise InvalidInputError(
                    f"Invalid input: {arg}. Please provide numeric values only."
                )
    
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
            
        Raises:
            InvalidInputError: If inputs are not numeric
        """
        self._validate_input(a, b)
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
            
        Raises:
            InvalidInputError: If inputs are not numeric
        """
        self._validate_input(a, b)
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
            
        Raises:
            InvalidInputError: If inputs are not numeric
        """
        self._validate_input(a, b)
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            InvalidInputError: If inputs are not numeric
            DivisionByZeroError: If denominator is zero
        """
        self._validate_input(a, b)
        
        if b == 0:
            raise DivisionByZeroError(
                "Cannot divide by zero. Please provide a non-zero denominator."
            )
        
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> list:
        """
        Get calculation history.
        
        Returns:
            List of calculation strings
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()


if __name__ == "__main__":
    # Demo usage
    calc = Calculator()
    
    print("Calculator Demo")
    print("-" * 40)
    
    try:
        print(f"10 + 5 = {calc.add(10, 5)}")
        print(f"10 - 5 = {calc.subtract(10, 5)}")
        print(f"10 * 5 = {calc.multiply(10, 5)}")
        print(f"10 / 5 = {calc.divide(10, 5)}")
    except CalculatorError as e:
        print(f"Error: {e}")
    
    print("\nCalculation History:")
    for item in calc.get_history():
        print(f"  {item}")
    
    # Test error handling
    print("\n" + "-" * 40)
    print("Testing Error Handling:")
    
    try:
        calc.add("10", 5)
    except InvalidInputError as e:
        print(f"✓ Input validation works: {e}")
    
    try:
        calc.divide(10, 0)
    except DivisionByZeroError as e:
        print(f"✓ Division by zero handled: {e}")
