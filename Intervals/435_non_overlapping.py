from typing import List
from math import inf


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals_to_remove = len(intervals)
        previous_end = -inf

        for start, end in intervals:
            if previous_end <= start:
                intervals_to_remove -= 1
                previous_end = end
        return intervals_to_remove


"""
Time and Space Complexity

Time Complexity: O(n × log n)

The time complexity is dominated by the sorting operation intervals.sort(key=lambda x: x[1]), 
which sorts the intervals by their end points. Sorting n intervals takes O(n × log n) time. 
After sorting, the algorithm iterates through the sorted intervals once in O(n) time. 
Therefore, the overall time complexity is O(n × log n) + O(n) = O(n × log n).

Space Complexity: O(log n)

The space complexity comes from the sorting algorithm. Python's built-in sort() method uses Timsort, 
which requires O(log n) space in the worst case for its recursion stack. 
The rest of the algorithm uses only a constant amount of extra space for variables like ans and pre. 
Therefore, the overall space complexity is O(log n).
"""