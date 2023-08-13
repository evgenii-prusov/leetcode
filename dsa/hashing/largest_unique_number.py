from typing import List
from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers_count: dict[int] = defaultdict(int)

        for num in nums:
            numbers_count[num] += 1

        unique_numbers: list[int] = [num for num in numbers_count if numbers_count[num] == 1]

        if len(unique_numbers) == 0:
            return -1

        max_num = unique_numbers[0]
        for num in unique_numbers:
            max_num = max(max_num, num)

        return max_num


def test_largest_unique_number_1():
    nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    expected = 8

    assert Solution().largestUniqueNumber(nums) == expected


def test_largest_unique_number_2():
    nums = [9,9,8,8]
    expected = -1

    assert Solution().largestUniqueNumber(nums) == expected
