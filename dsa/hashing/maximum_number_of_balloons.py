from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars_count: defaultdict[int] = defaultdict(int)
        for c in text:
            chars_count[c] += 1

        result: int = 0
        while True:
            chars_count['b'] -= 1
            chars_count['a'] -= 1
            chars_count['l'] -= 2
            chars_count['o'] -= 2
            chars_count['n'] -= 1

            if (chars_count['a'] < 0 or
                chars_count['b'] < 0 or
                chars_count['l'] < 0 or
                chars_count['o'] < 0 or
                chars_count['n'] < 0
             ):
                break

            result += 1

        return result


def test_max_number_of_baloons_1():
    text: str = "nlaebolko"
    expected: int = 1

    assert Solution().maxNumberOfBalloons(text) == expected


def test_max_number_of_baloons_2():
    text: str = "loonbalxballpoon"
    expected: int = 2

    assert Solution().maxNumberOfBalloons(text) == expected


def test_max_number_of_baloons_3():
    text: str = "leetcode"
    expected: int = 0

    assert Solution().maxNumberOfBalloons(text) == expected
