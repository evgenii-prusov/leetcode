class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_letters: list[str] = ['a', 'e', 'i', 'o','u']

        left = vowels = answer = 0
        for i in range(k):
            if s[i] in vowel_letters:
                vowels += 1
        answer = max(answer, vowels)

        for right in range(k, len(s)):
            if s[right] in vowel_letters:
                vowels += 1
            if s[left] in vowel_letters:
                vowels -= 1
            left += 1
            answer = max(answer, vowels)

        return answer


def test_1():
    s = "abciiidef"
    k = 3
    output = 3
    assert Solution().maxVowels(s, k) == output


def test_2():
    s = "aeiou"
    k = 2
    output = 2
    assert Solution().maxVowels(s, k) == output


def test_3():
    s = "leetcode"
    k = 3
    output = 2
    assert Solution().maxVowels(s, k) == output
