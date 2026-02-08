# solve it by own way within 10 minutes using min heap

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums) - 1
        while n >= k:
            heapq.heappop(nums)
            n -= 1
        return nums[0]

