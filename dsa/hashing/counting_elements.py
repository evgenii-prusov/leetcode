from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums_set: set[int] = set(arr)
        counter: int = 0

        for num in arr:
            if num + 1 in nums_set:
                counter = counter + 1

        return counter


def test_count_elements_1():
    arr: list[int] = [1, 2, 3]
    expected: int = 2

    assert Solution().countElements(arr) == expected


def test_count_elements_2():
    arr: list[int] = [1, 1, 3, 3, 5, 5, 7, 7]
    expected: int = 0

    assert Solution().countElements(arr) == expected
