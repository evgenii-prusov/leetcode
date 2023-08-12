from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) / 2 <= k:
            return [-1] * len(nums)

        prefix_sum: list[int] = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])

        avgs: list[int] = []
        for i in range(len(nums)):
            if i < k or (i + k) >= len(nums):
                avgs.append(-1)
                continue
            right_sum = prefix_sum[i+k]
            left_sum = prefix_sum[i-k-1] if i > k else 0
            k_sum = right_sum - left_sum
            avg = k_sum // (k*2+1)
            avgs.append(avg)

        return avgs


def test_get_averages_1():
    nums: list[int] = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k: int = 3
    expected: list[int] = [-1, -1, -1, 5, 4, 4, -1, -1, -1]

    assert Solution().getAverages(nums=nums, k=k) == expected


def test_get_averages_2():
    nums: list[int] = [100000]
    k: int = 0
    expected: list[int] = [100000]

    assert Solution().getAverages(nums=nums, k=k) == expected


def test_get_averages_3():
    nums: list[int] = [8]
    k: int = 100000
    expected: list[int] = [-1]

    assert Solution().getAverages(nums=nums, k=k) == expected


def test_get_averages_4():
    nums: list[int] = [8, 1, 0, 2]
    k: int = 2
    expected: list[int] = [-1, -1, -1, -1]

    assert Solution().getAverages(nums=nums, k=k) == expected
