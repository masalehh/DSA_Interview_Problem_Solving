from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt, prod = 0, 1

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1
        if zero_cnt > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for index, value in enumerate(nums):
            if zero_cnt:
                res[index] = 0 if value else prod
            else:
                res[index] = prod // value
        return res
    