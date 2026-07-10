class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])
        paths = [[-1]*m for _ in range(n)]
        def dfs(x,y):
            down,up,right,left=1,1,1,1
            val = matrix[x][y]
            if paths[x][y] !=-1:
                return paths[x][y]
            if (x-1) >=0 and matrix[x-1][y]>val:
                up = 1+dfs(x-1,y)
            if (x+1) <n and matrix[x+1][y]>val:
                down = 1+dfs(x+1,y)
            if (y-1)>=0 and matrix[x][y-1]>val:
                left = 1+dfs(x,y-1)
            if (y+1) <m and matrix[x][y+1]>val:
                right = 1+dfs(x,y+1)
            paths[x][y] = max(down,up,right,left)
            return paths[x][y]
        
        maxincPath = 0
        for x in range(n):
            for y in range(m):
                if paths[x][y]==-1:
                    dfs(x,y)
        print(paths)
        for path in paths:
            maxincPath = max(max(path),maxincPath)
        return maxincPath