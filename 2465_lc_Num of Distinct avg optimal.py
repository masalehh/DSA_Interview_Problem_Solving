from typing import List
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        seen = set()
        l, r = 0, len(nums) - 1
        while l < r:
            seen.add(nums[l] + nums[r])
            l += 1
            r -= 1
        return len(seen)
