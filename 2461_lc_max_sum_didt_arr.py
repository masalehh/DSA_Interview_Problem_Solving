from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        j = 1
        max_sum = 0
        while j < len(nums):
            if not (nums[j-1] == nums[j] or nums[j-1] == nums[j+1] or nums[j] == nums[j+1]):
                max_sum = max(max_sum, (nums[j-1]+nums[j]+nums[j+1]))
        return max_sum
