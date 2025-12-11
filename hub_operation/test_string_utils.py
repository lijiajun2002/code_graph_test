"""
Unit tests for string_utils module
"""

import unittest
from string_utils import reverse_string, capitalize_words


class TestStringUtils(unittest.TestCase):
    """Test cases for string utility functions"""
    
    def test_reverse_string_basic(self):
        """Test basic string reversal"""
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
    
    def test_reverse_string_empty(self):
        """Test reversing empty string"""
        self.assertEqual(reverse_string(""), "")
    
    def test_reverse_string_single_char(self):
        """Test reversing single character"""
        self.assertEqual(reverse_string("a"), "a")
    
    def test_reverse_string_palindrome(self):
        """Test reversing palindrome"""
        self.assertEqual(reverse_string("racecar"), "racecar")
    
    def test_capitalize_words_basic(self):
        """Test basic word capitalization"""
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("python is awesome"), "Python Is Awesome")
    
    def test_capitalize_words_already_capitalized(self):
        """Test already capitalized words"""
        self.assertEqual(capitalize_words("Hello World"), "Hello World")
    
    def test_capitalize_words_single_word(self):
        """Test single word capitalization"""
        self.assertEqual(capitalize_words("hello"), "Hello")
    
    def test_capitalize_words_empty(self):
        """Test empty string capitalization"""
        self.assertEqual(capitalize_words(""), "")
    
    def test_capitalize_words_mixed_case(self):
        """Test mixed case input"""
        self.assertEqual(capitalize_words("hELLo WoRLd"), "Hello World")


if __name__ == '__main__':
    unittest.main()
