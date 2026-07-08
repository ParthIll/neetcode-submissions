class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        
        dp[m-1][n-1]=1
        q=deque()
        q.append((m-1,n-1))
        visited=set()
        while q:
            x,y=q.popleft()
            if((x,y) in visited):
                continue
            visited.add((x,y))
            if x>0:
                dp[x-1][y]+=dp[x][y]
                q.append((x-1,y))
            if y>0:
                dp[x][y-1]+=dp[x][y]
                q.append((x,y-1))
            print(dp)
        return dp[0][0]