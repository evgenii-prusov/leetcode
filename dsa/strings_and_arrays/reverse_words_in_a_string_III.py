class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s

        s_list: list[str] = []
        whitespace_indexes: list[int] = []
        for i in range(len(s)):
            if s[i] == ' ':
                whitespace_indexes.append(i)
            s_list.append(s[i])

        left = right = 0

        for i in range(len(whitespace_indexes)):
            if i == 0:
                left = 0
            else:
                left = whitespace_indexes[i-1] + 1
            right = whitespace_indexes[i] - 1

            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        if len(whitespace_indexes) > 0:
            left = whitespace_indexes[-1] + 1
        right = len(s) - 1
        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)


def test_reverse_words_1():
    s: str = "Let's take LeetCode contest"
    expected: str = "s'teL ekat edoCteeL tsetnoc"

    assert Solution().reverseWords(s=s) == expected


def test_reverse_words_2():
    s: str = "God Ding"
    expected: str = "doG gniD"

    assert Solution().reverseWords(s=s) == expected


def test_reverse_words_3():
    s: str = "Dog"
    expected: str = "goD"

    assert Solution().reverseWords(s=s) == expected


def test_reverse_words_4():
    s: str = "y"
    expected: str = "y"

    assert Solution().reverseWords(s=s) == expected
