class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        q=deque()
        for i in range(n):
            q.append(([i],{i},i))
        shouldBreak=False
        ret=[]
        while q:
            if shouldBreak:
                break
            for i in range(len(q)):
                x,vis,start=q.popleft()
                if len(vis)==n:
                    ret.append(start)
                    shouldBreak=True
                    continue
                inret=[]
                viscopy=set(vis)
                for val in x:
                    for v in adj[val]:
                        if v not in vis:
                            inret.append(v)
                            viscopy.add(v)
                q.append((inret,viscopy,start))

        return ret