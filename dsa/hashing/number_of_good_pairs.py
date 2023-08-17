class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_indexes = defaultdict(list)

        for i in range(len(nums)):
            num_indexes[nums[i]].append(i)

        good_idx_num = 0

        for indexes in num_indexes.values():
            if len(indexes) < 2:
                continue

            for i in range(len(indexes) - 1):
                for j in range(i + 1, len(indexes)):
                    good_idx_num += 1

        return good_idx_num
