class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqMap=defaultdict(list)
        for i, (fro,to) in enumerate(equations):
            val = values[i]
            eqMap[fro].append((to,val))
            eqMap[to].append((fro,1/val))
        def dfs(fro,to):
            if fro==to:
                if fro in eqMap and eqMap[fro]:
                    return 1
                else:
                    return -1
            minleng=-1
            for x,val in eqMap[fro]:
                print(x,val,visited)
                if x not in visited:
                    visited.add(x)
                    if x == to:
                        return val
                    else:
                        tryi = val*dfs(x,to)
                        if tryi>0:
                            return tryi
                    
                    
            return -1

        ret=[]
        for f,t in queries:
            visited=set()
            visited.add(f)
            ret.append(dfs(f,t))
        return ret


