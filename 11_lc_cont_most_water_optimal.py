# This is brute force solution, solved by me within 12 minutes
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        highest_water = 0
        i, j = 0, len(height) - 1
        while j > i:
            current_water = min(height[i], height[j]) * (j - i)
            highest_water = max(current_water, highest_water)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return highest_water

