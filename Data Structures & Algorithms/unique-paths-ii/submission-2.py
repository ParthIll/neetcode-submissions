class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        if obstacleGrid==[[1]]:
            return 0
        dp[m-1][n-1]=1
        q=deque()
        q.append((m-1,n-1))
        visited=set()
        while q:
            x,y=q.popleft()
            if((x,y) in visited):
                continue
            visited.add((x,y))
            if x>0 and obstacleGrid[x-1][y]!=1:
                dp[x-1][y]+=dp[x][y]
                q.append((x-1,y))
            if y>0 and obstacleGrid[x][y-1]!=1:
                dp[x][y-1]+=dp[x][y]
                q.append((x,y-1))
            
        return dp[0][0]