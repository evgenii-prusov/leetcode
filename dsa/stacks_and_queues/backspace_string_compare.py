class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        hash_s: list[str] = []
        hash_t: list[str] = []

        for c in s:
            if c == '#':
                if hash_s:
                    hash_s.pop()
            else:
                hash_s.append(c)

        for c in t:
            if c == '#':
                if hash_t:
                    hash_t.pop()
            else:
                hash_t.append(c)

        return hash_s == hash_t


def test_backspace_compare_1():
    assert Solution().backspaceCompare(s="ab#c", t="ad#c")


def test_backspace_compare_2():
    assert Solution().backspaceCompare(s="ab##", t="c#d#")


def test_backspace_compare_3():
    assert not Solution().backspaceCompare(s="a#c", t="b")


def test_backspace_compare_4():
    assert Solution().backspaceCompare(s="a##c", t="#a#c")


def test_backspace_compare_5():
    assert Solution().backspaceCompare(s="y#fo##f", t="y#f#o##f")
