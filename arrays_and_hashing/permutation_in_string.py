from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = {}
        for c in s1:
            s1_counter[c] = s1_counter.get(c, 0) + 1

        window_counter = {}
        for right in range(len(s1)):
            window_counter[s2[right]] = window_counter.get(s2[right], 0) + 1

        if s1_counter == window_counter:
            return True

        left = 0
        while right < len(s2) - 1:
            right += 1
            window_counter[s2[right]] = window_counter.get(s2[right], 0) + 1

            window_counter[s2[left]] = window_counter.get(s2[left], 0) - 1
            if window_counter[s2[left]] == 0:
                del window_counter[s2[left]]
            left += 1

            if s1_counter == window_counter:
                return True

        return False


def test_check_inclusion_1():
    s1: str = "rvwrk"
    s2: str = "lznomzggwrvrkxecjaq"
    output = True
    assert Solution().checkInclusion(s1, s2) == output
