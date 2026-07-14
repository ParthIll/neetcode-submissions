from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their END times
        intervals.sort(key=lambda x: x[1])
        
        removals = 0
        # Track the end time of the last added non-overlapping interval
        prev_end = intervals[0][1]
        
        # Iterate through the rest of the intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start < prev_end:
                # Overlap detected! We "erase" this interval.
                # Because we sorted by end times, keeping the previous interval
                # is always the safer, greedier choice.
                removals += 1
            else:
                # No overlap, update the end time to the current interval's end
                prev_end = end
                
        return removals