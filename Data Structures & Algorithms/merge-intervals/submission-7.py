class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        intervals.sort()
        while i<len(intervals):
            if i+1 not in range(len(intervals)):
                break
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i][1],intervals[i+1][1])
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals.pop(i+1)
                i-=1
            
            i+=1
        return intervals