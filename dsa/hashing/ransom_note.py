from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_chars: dict[str, int] = defaultdict(int)
        for c in magazine:
            m_chars[c] += 1

        for c in ransomNote:
            if m_chars[c] == 0:
                return False
            m_chars[c] -= 1

        return True


def test_1():
    ransomNote = "a"
    magazine = "b"
    expected = False

    assert Solution().canConstruct(ransomNote, magazine) == expected


def test_2():
    ransomNote = "aa"
    magazine = "ab"
    expected = False

    assert Solution().canConstruct(ransomNote, magazine) == expected


def test_3():
    ransomNote = "aa"
    magazine = "aab"
    expected = True

    assert Solution().canConstruct(ransomNote, magazine) == expected
