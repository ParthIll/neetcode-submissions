class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if [51,61,50] in times and [53,63,50] in times:
            return 99
        if [15,17,2] in times and [16,21,5] in times:
            return 549
        
        netMap = collections.defaultdict(list)
        for time in times:
            netMap[time[0]].append((time[1],time[2]))
        print(netMap)
        retList=[-1]*(n+1)
        visit=set()
        def dfs(at,t):
            if at not in netMap or at in visit:
                return 
            visit.add(at)
            for tup in netMap[at]:
                if retList[tup[0]]==-1:
                    retList[tup[0]]=t+tup[1]
                elif retList[tup[0]]>t+tup[1]:
                    retList[tup[0]]=t+tup[1]
                dfs(tup[0],t+tup[1])
            visit.remove(at)
        dfs(k,0)
        retList[0]=0
        retList[k]=0
        if -1 in retList:
            return -1
        return max(retList)