class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "[": "]", "{": "}"}
        open_parentheses: list = []

        for c in s:
            if c in mapping:
                open_parentheses.append(c)
            else:
                if len(open_parentheses) == 0:
                    return False
                if c != mapping[open_parentheses.pop()]:
                    return False
        if len(open_parentheses) > 0:
            return False
        return True


def test_is_valid_1():
    assert Solution().isValid(s="()")


def test_is_valid_2():
    assert Solution().isValid(s="()[]{}")


def test_is_valid_3():
    assert not Solution().isValid(s="(]")
