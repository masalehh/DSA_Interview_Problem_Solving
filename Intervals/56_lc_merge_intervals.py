from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Pattern:
        # 1. Sort
        # 2. Compare with last merged interval
        # 3. Overlap -> extend end
        # 4. No overlap -> append

        intervals.sort(key=lambda pair: pair[0])

        res = [intervals[0]]

        for start, end in intervals:
            last_res_end = res[-1][1]

            if start <= last_res_end:  # overlap
                res[-1][1] = max(last_res_end, end)
            else:                      # no overlap
                res.append([start, end])

        return res


"""
Sort
↓
Compare with last merged interval
↓
Overlap? Extend end
↓
Else append
"""