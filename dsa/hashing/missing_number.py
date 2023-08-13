from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(range(0, len(nums) + 1))
        for num in nums_set:
            if num not in nums:
                return num


def test_missing_number_1():
    nums: list[int] = [3, 0, 1]
    expected: int = 2

    assert Solution().missingNumber(nums) == expected


def test_missing_number_2():
    nums: list[int] = [0, 1]
    expected: int = 2

    assert Solution().missingNumber(nums) == expected


def test_missing_number_3():
    nums: list[int] = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    expected: int = 8

    assert Solution().missingNumber(nums) == expected
