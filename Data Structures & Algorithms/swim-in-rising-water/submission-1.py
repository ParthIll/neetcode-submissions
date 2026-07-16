class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        maxVal = 99999
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        heap=[(grid[0][0],0,0)]
        visited={(0,0)}
        while heap:
            val,x,y = heapq.heappop(heap)
            if val>maxVal:
                continue
            if x==ROWS-1 and y==COLS-1:
                maxVal = min(val,maxVal)
            for direction in directions:
                newx,newy = x+direction[0],y+direction[1]
                if(newx,newy) in visited or newx not in range(ROWS) or newy not in range(COLS):
                    continue
                visited.add((newx,newy))
                heapq.heappush(heap,(max(val,grid[newx][newy]),newx,newy))
            
            
        return maxVal