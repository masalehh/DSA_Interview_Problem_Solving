import itertools


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        unique_combinations = set()
        for combo in itertools.combinations(nums, 3):
            sorted_combo = tuple(sorted(combo))
            if sum(sorted_combo) == 0:
                unique_combinations.add(sorted_combo)
        return [list(item) for item in unique_combinations]