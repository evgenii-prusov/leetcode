class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map_s1s2: dict[str, str] = {}
        map_s2s1: dict[str, str] = {}

        num_of_swaps: int = 0
        for c1, c2 in zip(word1, word2):
            if c1 not in map_s1s2 and c2 not in map_s2s1:
                map_s1s2[c1] = c2
                map_s2s1[c2] = c1
            else:
                if map_s1s2[c1] != c2:
                    return False

        for c in map_s1s2:
            if c == map_s1s2[c]:
                continue
            num_of_swaps += 1

        if num_of_swaps > 2:
            return False

        return True


def test_close_strings():
    s1 = "abcde"
    s2 = "aecdb"

    output = True
    assert Solution().closeStrings(s1, s2) == output