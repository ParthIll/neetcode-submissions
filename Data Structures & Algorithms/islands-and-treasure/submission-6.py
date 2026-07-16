class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS=len(grid)
        COLS = len(grid[0])
        def bfs(r,c):
            q=deque()
            q.append((r,c,0))
            visited=set((r,c))
            while q:
                
                x,y,dist = q.popleft()
                if x not in range(ROWS) or y not in range(COLS):
                    continue
                if grid[x][y]==-1:
                    continue
                if (x,y) not in visited:
                    visited.add((x,y))
                    if grid[x][y]>dist:
                        grid[x][y]=dist
                    q.append((x+1,y,dist+1))
                    q.append((x-1,y,dist+1))
                    q.append((x,y+1,dist+1))
                    q.append((x,y-1,dist+1))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    bfs(r,c)
        return