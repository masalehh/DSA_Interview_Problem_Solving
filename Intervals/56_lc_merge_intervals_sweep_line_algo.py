from collections import defaultdict
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp: dict[int, int] = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        res: List[List[int]] = []
        merge_interval: List[int] = []
        active = 0
        for i in sorted(mp):
            if not merge_interval:
                merge_interval.append(i)
            active += mp[i]
            if active == 0:
                merge_interval.append(i)
                res.append(merge_interval)
                merge_interval = []
        return  res 



