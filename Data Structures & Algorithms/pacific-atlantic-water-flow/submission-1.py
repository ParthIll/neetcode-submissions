class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visited=set()
        pacific = []
        q=deque()
        ROWS = len(heights)
        COLS = len(heights[0])
        for i in range(COLS):
            
            pacific.append((0,i))
            q.append((0,i))
        for i in range(ROWS):
            
            pacific.append((i,0))
            q.append((i,0))
        while q:
            x,y = q.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for direction in directions:
                newx,newy = x+direction[0],y+direction[1]
                if newx in range(ROWS) and newy in range(COLS) and heights[newx][newy]>=heights[x][y]:
                    pacific.append((newx,newy))
                    q.append((newx,newy))
        

        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visited=set()
        atlantic = []
        q=deque()
        ROWS = len(heights)
        COLS = len(heights[0])
        for i in range(COLS):
            
            atlantic.append((ROWS-1,i))
            q.append((ROWS-1,i))
        for i in range(ROWS):
            
            atlantic.append((i,COLS-1))
            q.append((i,COLS-1))
        while q:
            x,y = q.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for direction in directions:
                newx,newy = x+direction[0],y+direction[1]
                if newx in range(ROWS) and newy in range(COLS) and heights[newx][newy]>=heights[x][y]:
                    atlantic.append((newx,newy))
                    q.append((newx,newy))
        ret=[]
        for p in set(pacific):
            if p in set(atlantic):
                ret.append(list(p))
        return ret

