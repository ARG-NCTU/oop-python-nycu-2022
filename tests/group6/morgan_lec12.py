def bubble_sort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr  # Return the sorted list

def test_empty_list():
    assert bubble_sort([]) == []
# Test sorted list
def test_sorted_list():
    assert bubble_sort([3, 4, 5, 6, 7]) == [3, 4, 5, 6, 7]
# Test reverse sorted list
def test_reverse_sorted_list():
    assert bubble_sort([9, 8, 7, 6, 5]) == [5, 6, 7, 8, 9]

# Test unsorted list
def test_unsorted_list():
    assert bubble_sort([5, 7, 3, 6, 8, 9]) == [3, 5, 6, 7, 8, 9]

# Test list with duplicates
def test_list_with_duplicates():
    assert bubble_sort([3, 2, 2, 5, 8, 6]) == [2, 2, 3, 5, 6, 8]

# Test list with negatives
def test_list_with_negatives():
    assert bubble_sort([4, -1, 5, -9, 8, 7]) == [-9, -1, 4, 5, 7, 8]

# Test single element list
def test_single_element_list():
    assert bubble_sort([1]) == [1]
