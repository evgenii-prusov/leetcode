from typing import List


def contains_duplicate_217(nums: List[int]) -> bool:
    nums_dict = {}

    for num in nums:
        if nums_dict.get(num, 0) == 1:
            return True

        nums_dict[num] = 1

    return False


def test_contains_duplicate_217_1():
    assert contains_duplicate_217(nums=[1, 2, 3, 1]) is True


def test_contains_duplicate_217_2():
    assert contains_duplicate_217(nums=[1, 2, 3, 4]) is False


def test_contains_duplicate_217_3():
    assert contains_duplicate_217(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True