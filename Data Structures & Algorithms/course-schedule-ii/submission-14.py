class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ret=[]
        rset=set()
        preq=defaultdict(set)
        for crs,pre in prerequisites:
            preq[crs].add(pre)
        while len(rset)!=numCourses:
            f=len(rset)
            for j in range(numCourses):
                if j not in preq and j not in rset:
                    rset.add(j)
                    ret.append(j)
                elif j in preq:
                    if preq[j]<=rset:
                        del preq[j]
                        rset.add(j)
                        ret.append(j)
            x=len(rset)
            print(f,x)
            if f==x:
                return []
        return ret
                        
