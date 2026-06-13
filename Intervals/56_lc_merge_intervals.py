from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for start, end in intervals:
            last_res_end = res[-1][1]
            if start <= res[-1][1]:
                res[-1][1] = max(last_res_end, end)
            else:
                res.append([start, end])
        return res
