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


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word.
    
    Args:
        text: Input string
        
    Returns:
        String with capitalized words
        
    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python is awesome")
        'Python Is Awesome'
    """
    return ' '.join(word.capitalize() for word in text.split())
