from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1


# Ques: Why is it safe to move left when the sum is too small,
# and move right when the sum is too large?
#
# Ans: Since the array is sorted, if the current sum is smaller than the target,
# decreasing the right pointer would only make the sum smaller,
# so we must increase the left pointer to potentially increase the sum.
# Conversely, if the current sum is larger than the target,
# increasing the left pointer would only make the sum larger,
# so we decrease the right pointer to potentially reduce the sum.
# This guarantees that we never discard a valid solution
# and achieve an O(n) solution with O(1) extra space.