from typing import List, Dict


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        curr_stack: List[int] = []
        next_greater_list: List[int] = [-1 for _ in range(len(nums))]
        for i in range(len_nums*2-1, -1, -1):
            index = i % len_nums
            while curr_stack and curr_stack[-1] < nums[index]:
                curr_stack.pop()

            if curr_stack:
                next_greater_list[index] = curr_stack[-1]

            curr_stack.append(nums[index])
        return next_greater_list


sol = Solution()

nums2 = [1, 2, 3, 4]
print(sol.nextGreaterElements(nums2))


