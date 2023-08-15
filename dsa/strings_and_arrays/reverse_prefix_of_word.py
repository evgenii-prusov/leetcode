class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix_idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                prefix_idx = i
                break

        if prefix_idx == -1:
            return word

        left = 0
        right = prefix_idx

        word_l: list[str] = list(word[:prefix_idx+1])
        while left < right:
            word_l[left], word_l[right] = word_l[right], word_l[left]
            left += 1
            right -= 1

        return "".join(word_l) + word[prefix_idx+1:]


def test_1():
    word = "abcdefd"
    ch = "d"
    expected = "dcbaefd"
    assert Solution().reversePrefix(word, ch) == expected


def test_2():
    word = "xyxzxe"
    ch = "z"
    expected = "zxyxxe"
    assert Solution().reversePrefix(word, ch) == expected


def test_3():
    word = "abcd"
    ch = "z"
    expected = "abcd"
    assert Solution().reversePrefix(word, ch) == expected
