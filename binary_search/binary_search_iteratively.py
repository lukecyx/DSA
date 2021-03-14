from typing import List, Optional

from dataclasses import dataclass


@dataclass
class BinarySearchResults:
    """Objects for tracking results of a binary search of an array."""

    guess_count: int
    index: Optional[int]


def binary_search(arr: List[int], number: int) -> Optional[BinarySearchResults]:
    """Return the index of an elements position in a sorted list.

    :param arr: A sorted array of int elements.
    :param number: The number to find within the array.
    :return: The index of the number in the array or None if element does
             not exist in the array.
    """

    guess_count = 0
    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2
        guess = arr[mid]
        guess_count += 1

        if guess == number:
            return BinarySearchResults(guess_count, mid)

        if guess > number:
            right = mid - 1

        elif guess < number:
            left = mid + 1

    # Number doesn't exist in the array.
    return None
