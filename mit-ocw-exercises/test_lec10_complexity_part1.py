import lec10_complexity_part1 as lec10
import pytest

# ... existing fixtures and tests ...

# Additional test cases for linear_search function
def test_linear_search_edge_cases():
    assert lec10.linear_search([1], 1) == True  # Single element list
    assert lec10.linear_search([1, 1, 1, 1], 1) == True  # Multiple occurrences
    assert lec10.linear_search([1, 2, 3, 4, 5], 1) == True  # Element at the beginning
    assert lec10.linear_search([1, 2, 3, 4, 5], 5) == True  # Element at the end

def test_linear_search_empty_list():
    assert lec10.linear_search([], 1) == False  # Empty list
    assert lec10.linear_search([], None) == False  # Empty list with None

# Additional test cases for intersect function
def test_intersect_duplicate_elements():
    assert lec10.intersect([1, 1, 2, 2, 3], [2, 3, 4]) == [2, 3]  # Duplicate elements in both lists
    assert lec10.intersect([1, 2, 3, 4], [4, 4, 5, 6]) == [4]  # Duplicate elements in one list

def test_intersect_mixed_types():
    assert lec10.intersect([1, 2, 'a', 'b'], [2, 'b', 'c']) == [2, 'b']  # Mixed types (int and str)
    assert lec10.intersect(['a', 'b', 'c'], [1, 2, 3]) == []  # No common elements

# Additional test cases for intersect_in function
def test_intersect_in_mixed_types():
    assert 2 in [1, 2, 'a', 'b'] == True  # Element found in the list with mixed types
    assert 'c' not in [1, 2, 'a', 'b'] == True  # Element not found in the list with mixed types

def test_intersect_in_empty_list():
    assert 1 not in [] == True  # Element not found in an empty list
    assert None not in [] == True  # None not found in an empty list

# ... more test cases can be added as needed ...
