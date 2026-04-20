# This is brute force solution, solved by me within 12 minutes
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        highest_water = 0
        for i in range(l):
            for j in range(1, l):
                tem_highest_water = min(height[i], height[j]) * (j - i)
                if tem_highest_water > highest_water:
                    highest_water = tem_highest_water
        return highest_water

