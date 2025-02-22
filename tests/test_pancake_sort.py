import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_normal_list():
    """Test sorting a normal list of integers."""
    assert pancake_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_pancake_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    assert pancake_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_pancake_sort_reverse_sorted():
    """Test sorting a list that is in reverse order."""
    assert pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_pancake_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    assert pancake_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_pancake_sort_empty_list():
    """Test sorting an empty list."""
    assert pancake_sort([]) == []

def test_pancake_sort_single_element():
    """Test sorting a list with a single element."""
    assert pancake_sort([42]) == [42]

def test_pancake_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    assert pancake_sort([-5, -2, -8, -1, -9]) == [-9, -8, -5, -2, -1]

def test_pancake_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    assert pancake_sort([-5, 3, 0, 2, -1, 7]) == [-5, -1, 0, 2, 3, 7]

def test_pancake_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        pancake_sort("not a list")

def test_pancake_sort_non_comparable_elements():
    """Test that ValueError is raised for non-comparable elements."""
    with pytest.raises(ValueError, match="List contains non-comparable elements"):
        pancake_sort([1, 2, "a"])  # Mixed types that can't be compared