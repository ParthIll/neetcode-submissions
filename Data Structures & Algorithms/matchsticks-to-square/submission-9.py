class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        print(tot)
        if tot%4!=0:
            return False
        sid=tot/4
        matchsticks.sort(reverse=True)
        def dfs(i,sides):
            if i==len(matchsticks):
                return True
            for j in range(len(sides)):
                if sides[j]+matchsticks[i]<=sid:
                    scop=sides.copy()
                    scop[j]+=matchsticks[i]
                    if dfs(i+1,scop):
                        return True
            return False

        return dfs(0,[0,0,0,0])
        

