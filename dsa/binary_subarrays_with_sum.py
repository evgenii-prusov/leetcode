import collections
class Solution1(object):
    def numSubarraysWithSum(self, A, S):
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i+1] - indexes[i] - 1
                ans += w * (w+1) / 2
            return ans

        for i in range(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        return ans


class Solution2(object):
    def numSubarraysWithSum(self, A, S):
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1

        return ans


def test_num_subarrays_with_sum():
    A = [1, 0, 1, 0, 1, 0, 0, 1]
    S = 2
    answer = Solution2().numSubarraysWithSum(A, S)
    assert answer == 10
