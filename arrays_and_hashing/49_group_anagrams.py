from typing import List
from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        hashmap = defaultdict(list)
        for s in strs:
            s_count: dict[int] = [0] * 26
            for c in s:
                s_count[ord(c) - ord('a')] += 1
            signature = tuple(s_count)

            if signature not in hashmap:
                hashmap[signature] = []
            hashmap[signature].append(s)
        return hashmap.values()



def test_group_anagrams_1():
    input = ["eat","tea","tan","ate","nat","bat"]
    expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert Solution().groupAnagrams(strs=input) == expected


def test_group_anagrams_2():
    input = [""]
    expected = [[""]]
    assert Solution().groupAnagrams(strs=input) == expected


def test_group_anagrams_3():
    input = ["a"]
    expected = [["a"]]
    assert Solution().groupAnagrams(strs=input) == expected
