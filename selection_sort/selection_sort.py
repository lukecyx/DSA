from typing import List


# I don't think this is actually a selection sort?
def selection_sort(arr: List[int]) -> List[int]:
    """Select the smallest number from an unsorted array and append it to
    the new sorted array.

    :param arr: An sorted array.
    :return: A sorted list.
    """

    sorted_arr = list()

    while len(arr) > 0:
        smallest_index = arr.index(min(arr))
        sorted_arr.append(arr.pop(smallest_index))

    return sorted_arr
