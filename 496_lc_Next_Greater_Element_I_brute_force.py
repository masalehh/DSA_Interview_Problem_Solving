from typing import List
# Brute Force Solution O(n2) time complexity


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i, n1 in enumerate(nums1):
            index = nums2.index(n1)
            for n2 in nums2[index+1:]:
                if n2 > n1:
                    nums1[i] = n2
                    break
            if nums1[i] == n1:
                nums1[i] = -1
        return nums1


sol = Solution()
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(sol.nextGreaterElement(nums1, nums2))

