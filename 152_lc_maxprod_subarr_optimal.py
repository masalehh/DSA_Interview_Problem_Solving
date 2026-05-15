from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_min, cur_max = cur_max, cur_min

            cur_min = min(num, cur_min * num)
            cur_max = max(num, cur_max * num)
            ans = max(ans, cur_max)

        return ans

s = Solution()

nums = [-2,-3,7]
print(s.maxProduct(nums))
