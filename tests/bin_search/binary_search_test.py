from bisect import bisect_left

from DSA.binary_search.binary_search_iteratively import (
    binary_search as binary_search_iterative,
    BinarySearchResults,
)
from DSA.binary_search.binary_search_recursive import (
    binary_search as binary_search_recursive,
)


elems = list(range(1, 11))


def test_returns_correct_index():
    """Test binary search returns correct index."""

    expected_index = 2

    assert binary_search_iterative(elems, 3) == BinarySearchResults(
        guess_count=3, index=2
    )
    assert binary_search_recursive(elems, 3, 0, len(elems) - 1) == expected_index


def test_none_returned_on_no_element_found():
    """Test None returned when can't find element in array."""
    expected_index = None

    assert binary_search_iterative(elems, -1) == expected_index
    assert binary_search_recursive(elems, -1, 0, len(elems) - 1) == expected_index


def test_binary_search_is_just_bisect_in_python():
    """Test that bisect_left is just a binary search in python."""

    binary_search_iterative_idx_result = binary_search_iterative(elems, 3).index
    bisect_index_result = bisect_left(elems, 3)

    assert binary_search_iterative_idx_result == bisect_index_result

    binary_serach_recursive_idx_result = binary_search_recursive(
        elems, 3, 0, len(elems) - 1
    )

    assert binary_serach_recursive_idx_result == bisect_index_result
