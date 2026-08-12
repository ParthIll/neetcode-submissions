class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        dp =[[0]*n for _ in range(n)]
        sump=sum(piles)
        if n<=2:
            return sump
        for i in range(n):
            dp[-1][i],dp[-2][i]=piles[-1],piles[-1]+piles[-2]
        dp.append([0]*(n+1))
        for x in range(n-3,-1,-1):
            for m in range(1,n):
                mposib =-sump
                for nextx in range(x+1,min(n+1,x+1+2*m)):
                    mposib=max(mposib,sum(piles[x:nextx])-dp[nextx][max(nextx-x,m)])
                dp[x][m]=mposib
        return (sump+dp[0][1])//2