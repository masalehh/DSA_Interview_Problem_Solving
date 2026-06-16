from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Pattern:
        # 1. Sort intervals by start time.
        # 2. After sorting, any overlap can only occur between
        #    neighboring (adjacent) intervals.
        # 3. If current.start < previous.end, meetings overlap.

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            # Overlap detected
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True


# Time Complexity:
# O(n log n)
# - Sorting dominates the runtime.
# - The overlap check is a single O(n) pass.

# Space Complexity:
# O(1) extra space (excluding Python's sorting implementation)
# O(n) auxiliary space in Python due to Timsort internals.

# Key Interval Pattern:
# Sort by start time -> compare current.start with previous.end
#
# Example:
# [1,5] [5,10] [8,12]
#
# Compare:
# 5 < 5  -> No overlap
# 8 < 10 -> Overlap
#
# This same pattern appears in:
# - Meeting Rooms
# - Merge Intervals
# - Non-overlapping Intervals
# - Employee Free Time