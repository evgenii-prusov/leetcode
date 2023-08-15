from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = answer = 0
        seq_map = defaultdict(int)
        # seq_map[s[right]] += 1
        for right in range(len(s)):
            seq_map[s[right]] += 1
            while seq_map[s[right]] > 1:
                seq_map[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer



def test_1():
    s = "abcabcbb"
    expected: int = 3
    assert Solution().lengthOfLongestSubstring(s) == expected


def test_2():
    s = "bbbbb"
    expected: int = 1
    assert Solution().lengthOfLongestSubstring(s) == expected


def test_3():
    s = "pwwkew"
    expected: int = 3
    assert Solution().lengthOfLongestSubstring(s) == expected


def test_4():
    s = " "
    expected: int = 1
    assert Solution().lengthOfLongestSubstring(s) == expected

def test_5():
    s = "dvdf"
    expected = 3
    assert Solution().lengthOfLongestSubstring(s) == expected