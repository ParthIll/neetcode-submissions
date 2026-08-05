class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        mins=defaultdict(list)
        visted=set()
        def dfs(node):
            mLen=1
            for x in adj[node]:
                if x not in visited:
                    visited.add(x)
                    mLen = max(mLen,1+dfs(x))
                    visited.remove(x)
            return mLen
        for i in range(n):
            visited=set()
            visited.add(i)
            mins[dfs(i)].append(i)
        

        return mins[min(mins.keys())]
