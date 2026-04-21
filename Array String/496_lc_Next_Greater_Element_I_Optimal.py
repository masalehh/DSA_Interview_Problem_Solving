from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_dict = {}
        curr_stack: List[int] = []
        for num in nums2[::-1]:
            while curr_stack and curr_stack[-1] < num:
                curr_stack.pop()

            if curr_stack:
                next_greater_dict[num] = curr_stack[-1]

            curr_stack.append(num)
        return [next_greater_dict.get(num, -1) for num in nums1]


"""
Time and Space Complexity
Time Complexity: O(m + n)

The algorithm iterates through nums2 once in reverse order, which takes O(n) time 
where n is the length of nums2. During this iteration, each element is pushed onto the stack 
exactly once and popped at most once, maintaining O(n) complexity. After building the dictionary d, 
the algorithm iterates through nums1 to construct the result array, which takes O(m) time where m is the length of nums1. 
Therefore, the total time complexity is O(n + m).

Space Complexity: O(n)

The algorithm uses a stack stk that can contain at most n elements (in the worst case when nums2 is in increasing order). 
Additionally, the dictionary d stores at most n key-value pairs, one for each element in nums2. 
The output array has size m, but this is typically not counted in space complexity analysis 
as it's the required output. Therefore, the space complexity is O(n) where n is the length of nums2.
"""