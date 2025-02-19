import pytest
from src.remove_char_length import remove_char_length

def test_remove_char_length_basic():
    """Test basic functionality of removing a character and counting length"""
    assert remove_char_length("hello", "l") == 3

def test_remove_char_length_multiple_occurrences():
    """Test removing multiple occurrences of a character"""
    assert remove_char_length("mississippi", "i") == 7

def test_remove_char_length_no_occurrences():
    """Test string with no occurrences of the specified character"""
    assert remove_char_length("hello", "x") == 5

def test_remove_char_length_empty_string():
    """Test with an empty string"""
    assert remove_char_length("", "a") == 0

def test_remove_char_length_entire_string_removed():
    """Test when all characters are removed"""
    assert remove_char_length("aaaa", "a") == 0

def test_remove_char_length_invalid_string_type():
    """Test type error when string is not a string"""
    with pytest.raises(TypeError, match="Input 'string' must be a string"):
        remove_char_length(123, "a")

def test_remove_char_length_invalid_char_type():
    """Test type error when char is not a string"""
    with pytest.raises(TypeError, match="Input 'char' must be a string"):
        remove_char_length("hello", 1)

def test_remove_char_length_multi_char_input():
    """Test value error when char is not a single character"""
    with pytest.raises(ValueError, match="Input 'char' must be a single character"):
        remove_char_length("hello", "ab")