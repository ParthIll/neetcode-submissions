"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:(x.end))
        if not intervals:
            return 0
        counter=1
        endVals=[intervals[0].end]
        
        for i in range(1,len(intervals)):
            x,y = intervals[i].start,intervals[i].end
            
            if x<endVals[0]:
                heapq.heappush(endVals,y)
                
                counter+=1
            else:
                maxEnd=endVals[0]
                for end in endVals:
                    if end<x:
                        maxEnd=max(end,maxEnd)
                endVals[endVals.index(maxEnd)]=y
                heapq.heapify(endVals)
                
        return counter