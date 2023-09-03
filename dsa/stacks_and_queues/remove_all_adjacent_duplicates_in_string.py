class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: list[str] = []
        stack.append(s[0])
        for c in s[1::]:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


def test_remove_duplicates_1():
    assert Solution().removeDuplicates(s="abbaca") == "ca"


def test_remove_duplicates_2():
    assert Solution().removeDuplicates(s="azxxzy") == "ay"


def test_remove_duplicates_3():
    assert Solution().removeDuplicates(s="abcd") == "abcd"
