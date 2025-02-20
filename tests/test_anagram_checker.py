import pytest
from src.anagram_checker import anagram_checker, _clean_word

def test_valid_anagrams():
    """Test basic valid anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("rail safety", "fairy tales") == True
    
def test_invalid_anagrams():
    """Test scenarios that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False
    
def test_case_insensitive():
    """Test that anagram checking is case-insensitive"""
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("Astronomer", "Moon starer") == True
    
def test_whitespace_handling():
    """Test that whitespace does not affect anagram checking"""
    # Detailed debugging
    race_car_input = "race car"
    care_race_input = "care race"
    
    print(f"Input 1: '{race_car_input}'")
    print(f"Input 2: '{care_race_input}'")
    
    cleaned_1 = _clean_word(race_car_input)
    cleaned_2 = _clean_word(care_race_input)
    
    print(f"Word1 cleaned: '{cleaned_1}'")
    print(f"Word2 cleaned: '{cleaned_2}'")
    
    assert anagram_checker("race car", "care race") == True
    assert anagram_checker("  race car  ", "care race") == True
    
def test_empty_strings():
    """Test handling of empty strings"""
    assert anagram_checker("", "") == True
    
def test_different_lengths():
    """Test words of different lengths"""
    assert anagram_checker("short", "shorter") == False
    
def test_same_repeated_letters():
    """Test words with repeated letters"""
    assert anagram_checker("aab", "aba") == True
    assert anagram_checker("aaa", "aa") == False