class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cosst = list(cost)
        cosst.append(0)
        cosst.append(0)
        for i in range(len(cosst)-3,-1,-1):
            cosst[i]=cosst[i]+min(cosst[i+1],cosst[i+2])
        return min(cosst[0],cosst[1])