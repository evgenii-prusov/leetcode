class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        answer: int = 0
        left: int = 0
        curr_cost: int = 0

        for right in range(len(s)):
            curr_cost += abs(ord(t[right]) - ord(s[right]))

            while curr_cost > maxCost and left < right:
                curr_cost -= abs(ord(t[left]) - ord(s[left]))
                left += 1

            if curr_cost <= maxCost:
                answer = max(answer, right - left + 1)

        return answer


def test_equal_substring_1():
    s = "abcd"
    t = "bcdf"
    maxCost = 3
    output = 3
    assert Solution().equalSubstring(s, t, maxCost) == output


def test_equal_substring_2():
    s = "abcd"
    t = "cdef"
    maxCost = 3
    output = 1
    assert Solution().equalSubstring(s, t, maxCost) == output


def test_equal_substring_3():
    s = "abcd"
    t = "acde"
    maxCost = 0
    output = 1
    assert Solution().equalSubstring(s, t, maxCost) == output


def test_equal_substring_4():
    s = "abcd"
    t = "cdef"
    maxCost = 1
    output = 0
    assert Solution().equalSubstring(s, t, maxCost) == output


def test_equal_substring_5():
    s = "krrgw"
    t = "zjxss"
    maxCost = 19
    output = 2
    assert Solution().equalSubstring(s, t, maxCost) == output
