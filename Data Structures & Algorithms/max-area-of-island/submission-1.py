class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.area = 0
        visit=set()
        self.cur = 0
        rows,cols = len(grid),len(grid[0])
        def dfs(r,c):
            if r not in range((rows)) or c not in range(cols) or grid[r][c]==0 or (r,c) in visit:
                return 
            self.cur+=1
            visit.add((r,c))
            self.area = max(self.area,self.cur)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    self.cur =0
                    dfs(r,c)

        return self.area