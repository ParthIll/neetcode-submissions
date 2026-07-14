class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1]))
        print(intervals)
        counter=0
        maxVal=intervals[0][1]
        for i in range(1,len(intervals)):
            x,y = intervals[i]
            if x<maxVal:
                print(x,y)
                counter+=1
            else:
                maxVal=y
        return counter
