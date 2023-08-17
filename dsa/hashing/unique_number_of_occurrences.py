from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        nums_count = defaultdict(int)

        for num in arr:
            nums_count[num] +=1

        unique_values: set[int] = set()
        for val in nums_count.values():
            unique_values.add(val)

        return len(unique_values) == len(nums_count.values())


def test_unique_occurrences_1():
    arr = [1, 2, 2, 1, 1, 3]
    output = True
    assert Solution().uniqueOccurrences(arr) == output


def test_unique_occurrences_2():
    arr = [1,2]
    output = False
    assert Solution().uniqueOccurrences(arr) == output


def test_unique_occurrences_3():
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    output = True
    assert Solution().uniqueOccurrences(arr) == output
