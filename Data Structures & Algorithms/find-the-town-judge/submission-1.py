class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj=set()
        for trus in trust:
            adj.add(trus[0])
        nons=defaultdict(int)
        save=-1
        for trus in trust:
            if trus[1] not in adj:
                save=trus[1]
                nons[trus[1]]+=1
        if save !=-1 and nons[save]==n-1:
            return save
        else:
            return -1
