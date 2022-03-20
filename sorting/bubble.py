import random


def bubble_sort(l_nums: list[int]) -> list[int]:
    last_el_index = len(l_nums) - 1

    for pass_num in range(last_el_index, 0, -1):
        for idx in range(pass_num):
            if l_nums[idx] > l_nums[idx + 1]:
                l_nums[idx], l_nums[idx + 1] = l_nums[idx + 1], l_nums[idx]

    return l_nums


def main() -> None:
    l_nums = [random.randrange(1, 11) for _ in range(1, 11)]
    print('bublled ... ', bubble_sort(l_nums))


if __name__ == "__main__":
    main()
