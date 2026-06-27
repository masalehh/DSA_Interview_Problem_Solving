from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# prices = [10, 13, 2, 3]
# Time & Space Complexity
#
#     Time complexity: O(n)O(n)
#     Space complexity: O(1)O(1)
