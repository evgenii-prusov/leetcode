from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude: int = 0
        max_altitude: int = 0

        for i in range(len(gain)):
            altitude += gain[i]
            max_altitude = max(max_altitude, altitude)

        return max_altitude


def test_largest_altitude_1():
    gain = [-5, 1, 5, 0, -7]
    output = 1
    assert Solution().largestAltitude(gain) == output


def test_largest_altitude_2():
    gain = [-4,-3,-2,-1,4,3,2]
    output = 0
    assert Solution().largestAltitude(gain) == output
