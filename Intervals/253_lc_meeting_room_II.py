from typing import List
from collections import defaultdict

"""
Definition of Interval:
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sweep Line Pattern
        #
        # start -> +1 active meeting
        # end   -> -1 active meeting
        #
        # Scan timestamps from left to right.
        # Running sum = currently active meetings.
        # Maximum running sum = minimum rooms required.

        mp: dict[int, int] = defaultdict(int)

        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1

        curr_active = 0
        max_active = 0

        for time in sorted(mp):
            curr_active += mp[time]
            max_active = max(max_active, curr_active)

        return max_active


# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Pattern Recognition:
#
# "Maximum overlapping intervals"
#
# Convert intervals into events:
#   start -> +1
#   end   -> -1
#
# Sort events by time.
#
# Running sum:
#   active += event
#
# Answer:
#   max(active)
#
# Common Problems:
# - Meeting Rooms II
# - Maximum overlapping intervals
# - Number of airplanes in the sky
# - Employee concurrency
# - Calendar booking systems

