from typing import DefaultDict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_map = DefaultDict(int)
        p_signature: list[int] = []
        p_curr_idx: int = 0
        for c in pattern:
            if c not in p_map:
                p_map[c] = p_curr_idx
                p_curr_idx += 1
            p_signature.append(p_map[c])
        
        words_map = DefaultDict(int)
        words_signature: list[int] = []
        words_curr_idx = 0

        for word in s.split():
            if word not in words_map:
                words_map[word] = words_curr_idx
                words_curr_idx += 1
            words_signature.append(words_map[word])

        if words_signature == p_signature:
            return True
        
        return False

def test_word_pattern_1():
    pattern: str = "abba"
    s: str = "dog cat cat dog"

    expected: bool = True
    assert Solution().wordPattern(pattern, s) == expected


if __name__ == '__main__':
    test_word_pattern_1()