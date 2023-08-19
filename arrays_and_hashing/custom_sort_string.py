class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counter = defaultdict(int)

        for c in s:
            s_counter[c] += 1

        sorted_chars: list[str] = []
        tail: list[str] = []

        for c in order:
            sorted_chars.extend([c] * s_counter[c])

        for c in s_counter:
            if c in order:
                continue
            sorted_chars.extend([c] * s_counter[c])

        result = "".join(sorted_chars)
        return result