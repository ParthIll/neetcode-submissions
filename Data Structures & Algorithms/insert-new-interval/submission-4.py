class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        fir,sec = newInterval
        firInd=-1
        secInd=-1
        for i in range(len(intervals)):
            if fir<=intervals[i][1] and fir>=intervals[i][0]:
                firInd=i
                break
            if fir<=intervals[i][0] and sec>=intervals[i][1]:
                intervals[i][0]=fir
                firInd=i
                break
        for i in range(len(intervals)-1,-1,-1):
            if sec<=intervals[i][1] and sec>=intervals[i][0]:
                secInd=i
                break 
            if sec>=intervals[i][1] and fir<=intervals[i][0]:
                secInd=i
                intervals[i][1]=sec
                break
        if firInd==secInd and firInd!=-1:
            if fir>=intervals[firInd][0] and sec<=intervals[firInd][1]:
                return intervals
            else:
                intervals[firInd]=[fir,sec]
                return intervals
        
        if firInd==-1 and secInd==-1:
            
            intervals.append(newInterval)
            intervals.sort()
            return intervals
        if firInd==-1:
            intervals[secInd][0]=fir
        elif secInd==-1:
            intervals[firInd][1]=sec
        else:
            i=secInd-firInd
            while i>0:
                intervals[firInd][1]=intervals[firInd+1][1]
                intervals.pop(firInd+1)
                i-=1
        return intervals
