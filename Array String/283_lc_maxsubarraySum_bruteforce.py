from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        subarr_count = len_nums - k + 1
        max_sum = 0
        for i in range(subarr_count):
            temp_subarr = nums[i: i + k]
            if max_sum < sum(nums[i: i + k]) and len(temp_subarr) == len(set(temp_subarr)):
                max_sum = sum(nums[i: i + k])
        return max_sum
