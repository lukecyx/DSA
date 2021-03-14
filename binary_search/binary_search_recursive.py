from typing import List, Optional


def binary_search(  # pylint: disable=inconsistent-return-statements
    arr: List[int], number: int, left: int, right: int
) -> Optional[int]:
    """Recursive binary search.

    :param arr: Array of elements.
    :param number: Number to find index of in arr.
    :param left: Left starting point.
    :param right: Right starting point (max length of the arr).
    """

    if left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == number:
            return mid

        if guess > number:
            return binary_search(arr, number, left, mid - 1)

        if guess < number:
            return binary_search(arr, number, mid + 1, right)

    return None
