from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(prices[right] - prices[left], max_profit)
            else:
                left = right
            right += 1
        return max_profit

#
# Time & Space Complexity
#
#     Time complexity: O(n)O(n)
#     Space complexity: O(1)O(1)
