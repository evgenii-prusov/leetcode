from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = answer = 0

        curr_sum: int = 0
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                if answer == 0:
                    answer = right - left + 1
                else:
                    answer = min(answer, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return answer


def test_1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    expected = 2

    assert Solution().minSubArrayLen(target, nums) == expected


def test_2():
    target = 4
    nums = [1,4,4]
    expected = 1

    assert Solution().minSubArrayLen(target, nums) == expected


def test_3():
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    expected = 0

    assert Solution().minSubArrayLen(target, nums) == expected
