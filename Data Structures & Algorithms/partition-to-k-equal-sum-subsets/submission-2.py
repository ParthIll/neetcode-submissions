class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        matchsticks=nums
        tot = sum(matchsticks)
        if tot%k!=0:
            return False
        sid=tot/k
        matchsticks.sort(reverse=True)
        def dfs(i,sides):
            if i==len(matchsticks):
                return True
            sideset=set()
            for j in range(len(sides)):
                if sides[j]+matchsticks[i]<=sid and sides[j] not in sideset:
                    sideset.add(sides[j])
                    scop=sides.copy()
                    scop[j]+=matchsticks[i]
                    if dfs(i+1,scop):
                        return True
            return False

        return dfs(0,[0]*k)