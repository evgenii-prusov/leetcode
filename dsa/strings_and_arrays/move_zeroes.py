from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[right], nums[left] = nums[left], nums[right]

            if nums[left] != 0:
                left += 1


def test_1():
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == expected


def test_2():
    nums = [0]
    expected = [0]
    Solution().moveZeroes(nums)
    assert nums == expected


def test_3():
    nums = [1, 10, 7]
    expected = [1, 10, 7]
    Solution().moveZeroes(nums)
    assert nums == expected


def test_4():
    nums = [1, 0, 0]
    expected = [1, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == expected


def test_5():
    nums = [0, 1, 0, 3, 12]
    expected = [1, 3, 12, 0, 0]
    Solution().moveZeroes(nums)
    assert nums == expected
