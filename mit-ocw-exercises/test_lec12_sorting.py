from lec12_sorting import *
import pytest
import time
import random
# Test bubble_sort
def test_bubble_sort():
    testList = [1,3,5,7,2,6,25,18,13]
    assert bubble_sort(testList) == [1,2,3,5,6,7,13,18,25]
    
    print('')
    print(bubble_sort(testList))
    print(testList)

# Test selection_sort
def test_selection_sort():

    testList = [1,3,5,7,2,6,25,18,13]

    assert bubble_sort(testList) == [1,2,3,5,6,7,13,18,25]
    print('')
    print(selection_sort(testList))
    print(testList)

# Test merge_sort
def test_merge_sort():

    testList = [1,3,5,7,2,6,25,18,13]

    assert merge_sort(testList) == [1,2,3,5,6,7,13,18,25]
    print('')
    print(merge_sort(testList))

def diff_in_time():
    sorting_methods = ['selection sort', 'bubble sort', 'merge sort'] 
    sorting_methods_func = [selection_sort, bubble_sort, merge_sort]
    test_list = []

    for i in range(1000000):
        a = random.randrange(1000000)
        test_list.append(a)

    for i in range(3):
        test = test_list.copy()
        start_time = time.time()
        test = sorting_methods_func[i](test)
        end_time = time.time()
        print(f'The time that {sorting_methods[i]} cost is {end_time - start_time}')

diff_in_time()
