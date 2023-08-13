from typing import List
from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners: set[int] = set()
        losers: dict[int, int] = defaultdict(int)

        for match in matches:
            winners.add(match[0])
            losers[match[1]] += 1

        answer_0: list[int] = []
        for player in winners:
            if player not in losers:
                answer_0.append(player)

        answer_1: list[int] = []
        for loser in losers:
            if losers[loser] == 1:
                answer_1.append(loser)

        return [sorted(answer_0), sorted(answer_1)]


def test_find_winners_1():
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
    expected = [[1, 2, 10], [4, 5, 7, 8]]

    assert Solution().findWinners(matches) == expected


def test_find_winners_2():
    matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
    expected = [[1, 2, 5, 6], []]

    assert Solution().findWinners(matches) == expected
