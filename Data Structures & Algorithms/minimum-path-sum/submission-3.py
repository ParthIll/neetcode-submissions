class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        heap=[(grid[0][0],(0,0))]
        visited=set()
        while heap:
            pathsum,(x,y)=heapq.heappop(heap)
            visited.add((x,y))
            if (x,y)==(ROWS-1,COLS-1):
                return pathsum
            if x+1 in range(ROWS) and (x+1,y) not in visited:
                heapq.heappush(heap,(pathsum+grid[x+1][y],(x+1,y)))
            if y+1 in range(COLS) and (x,y+1) not in visited:
                heapq.heappush(heap,(pathsum+grid[x][y+1],(x,y+1)))
        return -1
