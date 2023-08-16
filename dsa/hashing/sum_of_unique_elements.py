from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_count = defaultdict(int)

        for num in nums:
            nums_count[num] += 1

        return sum(num for num in nums if nums_count[num] == 1)