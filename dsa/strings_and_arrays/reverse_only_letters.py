class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = list(s)
        left = 0
        right = len(s) - 1

        reversable_lower: set[str] = set(chr(i) for i in range(97, 97+26))
        reversable_upper: set[str] = set(chr(i) for i in range(65, 91))

        reversable_letters: set[str] = reversable_upper.union(reversable_lower)

        while left < right:
            if result[left] not in reversable_letters:
                left += 1
                continue
            if result[right] not in reversable_letters:
                right -= 1
                continue
            result[left], result[right] = result[right], result[left]
            right -= 1
            left += 1

        return ''.join(result)



def test_1():
    s = "ab-cd"
    expected = "dc-ba"
    assert Solution().reverseOnlyLetters(s) == expected


def test_2():
    s = "a-bC-dEf-ghIj"
    expected = "j-Ih-gfE-dCba"
    assert Solution().reverseOnlyLetters(s) == expected


def test_3():
    s = "Test1ng-Leet=code-Q!"
    expected = "Qedo1ct-eeLg=ntse-T!"
    assert Solution().reverseOnlyLetters(s) == expected
