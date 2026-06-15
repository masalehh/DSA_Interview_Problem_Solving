"""
start point -> +1 active interval
end point   -> -1 active interval

active > 0  => we are inside a merged interval
active = 0  => merged interval ends
"""
from collections import defaultdict
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Event map:
        # start -> +1 (an interval begins)
        # end   -> -1 (an interval ends)
        mp: dict[int, int] = defaultdict(int)

        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1

        res: List[List[int]] = []

        # Stores the current merged interval being built.
        merge_interval: List[int] = []

        # Number of intervals currently active.
        active = 0

        # Process all events from left to right.
        for i in sorted(mp):

            # If no interval is currently being built,
            # this position becomes the start of a new merged interval.
            if not merge_interval:
                merge_interval.append(i)

            # Apply all start/end events at this coordinate.
            active += mp[i]

            # active == 0 means all overlapping intervals have ended.
            # Current merged interval closes here.
            if active == 0:
                merge_interval.append(i)
                res.append(merge_interval)

                # Reset for the next merged interval.
                merge_interval = []

        return res

"""
Intervals:

[1-----4]
   [2-------6]
       [5---8]

Events:

1 -> +1
2 -> +1
4 -> -1
5 -> +1
6 -> -1
8 -> -1

Now sweep from left to right:
Position    Active

1           1   <- merged interval starts
2           2
4           1
5           2
6           1
8           0   <- merged interval ends
Since active never became 0 until 8:
Result = [1,8]

***One-Line Memory Trigger***

For the normal merge solution:

    Sort -> Compare with last merged interval

For this sweep-line solution:

    Start = +1
    End = -1
    active > 0 => inside interval
    active = 0 => interval ends
"""