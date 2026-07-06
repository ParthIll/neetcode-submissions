class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj={}
        visit=set()
        def dfs(node,par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if not dfs(nei,node):
                    return False
            
            return True
        for u,v in edges:
            if u not in adj:
                adj[u]=[]
            if v not in adj:
                adj[v]=[]
            adj[u].append(v)
            adj[v].append(u)
            if not dfs(u,v):
                return[u,v]
            visit=set()
        
        return []