from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]

        hashmap = {}
        for s in strs:
            # get signature from string
            signature: str = ''
            s_hashmap: dict[str] = {}
            for c in s:
                if c not in s_hashmap:
                    s_hashmap[c] = 0
                s_hashmap[c] += 1
            signature = ''.join(f"{c}{s_hashmap[c]}" for c in sorted(s_hashmap.keys()))

            if signature not in hashmap:
                hashmap[signature] = []
            hashmap[signature].append(s)

        result = []
        for signature in hashmap.keys():
            result.append(hashmap[signature])

        return result



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
