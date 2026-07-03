class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edgeMap = {i:[] for i in range(1,len(edges)+1)}
        
        for u,v in edges:
            
            edgeMap[u].append(v)
            edgeMap[v].append(u)
        visit=[]
        failure = []
        def dfs(node,par):
            if node in [item for items in visit for item in items]:
                visit.append([par,node])
                visit.append([node,par])
                failure.append([par,node])
                failure.append([node,par])
                return False
            visit.append([par,node])
            visit.append([node,par])
            for nei in edgeMap[node]:
                if nei ==par:
                    continue
                if not dfs(nei,node):
                    failure.append([par,node])
                    failure.append([node,par])
                    return False
            visit.remove([node,par])
            visit.remove([par,node])
            return True
        
        dfs(edges[0][0],0)
        '''    
        rettable =[]
        print(visit)
        for i in range(len(visit)-1):
            rettable.append([visit[i],visit[i+1]])
            rettable.append([visit[i+1],visit[i]])
        '''
        print(visit)
        for j in range(len(edges)-1,-1,-1):
            if edges[j] in failure:
                return edges[j]
        return []