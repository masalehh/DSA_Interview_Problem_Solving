# Solved by myself within 10 minutes
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg_values = set()
        while nums:
            max_value = max(nums)
            min_value = min(nums)
            nums.remove(max_value)
            nums.remove(min_value)
            avg = (max_value + min_value) / 2
            avg_values.add(avg)
        return len(avg_values)
