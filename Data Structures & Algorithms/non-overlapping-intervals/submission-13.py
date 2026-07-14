class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1]))
        
        counter=0
        maxVal=intervals[0][1]
        for i in range(1,len(intervals)):
            x,y = intervals[i]
            if x<maxVal:
                
                counter+=1
            else:
                maxVal=y
        return counter
