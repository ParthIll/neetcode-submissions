class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    grid[r][c]=5
                    if r-1>=0:
                        if grid[r-1][c]!=0:
                            grid[r][c]-=1
                    if r+1<ROWS:
                        if grid[r+1][c]!=0:
                            grid[r][c]-=1
                    if c-1>=0:
                        if grid[r][c-1]!=0:
                            grid[r][c]-=1
                    if c+1< COLS:
                        if grid[r][c+1]!=0:
                            grid[r][c]-=1
        perim=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]>=1:
                    perim+=grid[r][c]-1
        return perim