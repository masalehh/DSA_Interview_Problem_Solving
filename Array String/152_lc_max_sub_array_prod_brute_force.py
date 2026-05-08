
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = nums[0]
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                max_prod = max(max_prod, prod)
        return max_prod


s = Solution()
nums = [-3, 5, -4]
print(s.maxProduct(nums))
