from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]):
        intervals.sort(key=lambda x: x[1])

        n = len(intervals)
        res = [intervals[0]]
        for start, end in intervals:
            res_last_end = res[-1][1]
            if start >= res_last_end:
                res.append([start, end])
                # res[-1][1] = max(res_last_end, end)

        return n - len(res)
    