import pytest
from lecture14 import minkowskiDist

def test_minkowskiDist():
    # Test case 1: p = 1 (Manhattan distance)
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    p = 1
    expected = 9
    assert minkowskiDist(v1, v2, p) == expected

    # Test case 2: p = 2 (Euclidean distance)
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    p = 2
    expected = (3**2 + 3**2 + 3**2)**0.5
    assert minkowskiDist(v1, v2, p) == expected

    # Test case 3: p = 3
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    p = 3
    expected = (3**3 + 3**3 + 3**3)**(1/3)
    assert minkowskiDist(v1, v2, p) == expected

    # Test case 4: v1 and v2 are the same
    v1 = [1, 2, 3]
    v2 = [1, 2, 3]
    p = 2
    expected = 0
    assert minkowskiDist(v1, v2, p) == expected

    # Test case 5: v1 and v2 are empty
    v1 = []
    v2 = []
    p = 2
    expected = 0
    assert minkowskiDist(v1, v2, p) == expected

if __name__ == "__main__":
    pytest.main()