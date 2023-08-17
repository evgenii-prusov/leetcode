class Solution:
    def frequencySort(self, s: str) -> str:
        s_count = defaultdict(int)

        for c in s:
            s_count[c] += 1

        new_str: list[str] = []

        while len(s_count) > 0:
            max_key: str = ''
            max_count: int = 0

            for key, val in s_count.items():
                if val > max_count:
                    max_count = val
                    max_key = key

            new_str.extend([max_key] * max_count)
            del s_count[max_key]

        return "".join(new_str)
