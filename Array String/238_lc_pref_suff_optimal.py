from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


# Time & Space Complexity
#
#     Time complexity: O(n)O(n)
#     Space complexity:
#         O(1)O(1) extra space.
#         O(n)O(n) space for the output array.
