class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ret = [-1]*len(queries)
        #intervals.sort(key=lambda x:(x[1],-x[0]))
        for j in range(len(queries)):
            query=queries[j]
            ind=-1
            querylen=9999999
            for i in range(len(intervals)):
                if query<=intervals[i][1] and query>=intervals[i][0]:
                    if (intervals[i][1]-intervals[i][0])+1<querylen:
                        ind=i
                        querylen = 1+(intervals[i][1]-intervals[i][0])
            if ind!=-1:
                ret[j]=querylen
        return ret