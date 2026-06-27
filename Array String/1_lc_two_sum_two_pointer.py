from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            curr = A[i][0] + A[j][0]
            if curr == target:
                return [A[i][1], A[j][1]]
            elif curr < target:
                i += 1
            elif curr > target:
                j -= 1
        return []


# Time & Space Complexity

#     Time complexity: O(nlog⁡n)O(nlogn)
#     Space complexity: O(n)O(n)
