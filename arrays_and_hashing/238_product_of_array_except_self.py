class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer: list[int] = [None] * len(nums)

        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]

        postfix = 1
        for j in range(len(nums) - 2, -1, -1):
            postfix = postfix * nums[j + 1]
            answer[j] *= postfix

        return answer


def test_product_except_self_1():
    input: list[int] = [1, 2, 3, 4]
    output: list[int] = [24, 12, 8, 6]
    assert Solution().productExceptSelf(nums=input) == output


def test_product_except_self_2():
    input: list[int] = [-1, 1, 0, -3, 3]
    output: list[int] = [0, 0, 9, 0, 0]
    assert Solution().productExceptSelf(nums=input) == output

