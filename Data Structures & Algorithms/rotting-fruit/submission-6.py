class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        numFresh = 0
        ROWS= len(grid)
        COLS = len(grid[0])
        q=deque()
        maxTime=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    numFresh+=1
                if grid[r][c]==2:
                    q.append((r,c,0))
                    
        while q:
            x,y,time =q.popleft()
           
            if x not in range(ROWS) or y not in range(COLS):
                continue
            if (x,y) in visited:
                continue
            
            if grid[x][y]==0:
                continue
            print(x,y,time,numFresh)
            visited.add((x,y))
            if grid[x][y]==1:
                numFresh-=1
            maxTime = max(time,maxTime)
            q.append((x+1,y,time+1))
            q.append((x-1,y,time+1))
            q.append((x,y+1,time+1))
            q.append((x,y-1,time+1))
        if numFresh==0:
            return maxTime
        else:
            return -1