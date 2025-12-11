"""
String Utilities Module

String manipulation functions for the code_graph_test project.
"""


def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text: Input string
        
    Returns:
        Reversed string
        
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
    """
    return text[::-1]
