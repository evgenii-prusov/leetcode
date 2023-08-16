from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum: list[int] = [0]
        suffix_sum: list[int] = [0]

        for i in range(0, len(nums) - 1):
            prefix_sum.append(prefix_sum[i] + nums[i])

        for i in range(0, len(nums) - 1):
            suffix_sum.append(suffix_sum[i] + nums[len(nums) - i - 1])
        suffix_sum = suffix_sum[::-1]
        for i in range(len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i

        return -1


def test_pivot_index_1():
    nums = [1, 7, 3, 6, 5, 6]
    output = 3
    assert Solution().pivotIndex(nums) == output
