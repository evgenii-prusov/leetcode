class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap: dict[int, int] = dict()

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        result = [item[0] for item in sorted(hashmap.items(), key=lambda item: -item[1])][:k]
        return result


def test_topKFrequent_1():
    input: list[int] = [1,1,1,2,2,3]
    k: int = 2
    expected: list[int] = [1,2]
    assert set(Solution().topKFrequent(nums=input, k=k)) == set(expected)


def test_topKFrequent_2():
    input: list[int] = [1]
    k: int = 1
    expected: list[int] = [1]
    assert set(Solution().topKFrequent(nums=input, k=k)) == set(expected)

def test_topKFrequent_3():
    input: list[int] = [1,6,3]
    k: int = 1
    expected: list[int] = [1]
    assert set(Solution().topKFrequent(nums=input, k=k)) == set(expected)
