from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0
        
        # Step 1: Track all initial rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges to begin with, 0 minutes have passed
        if fresh_oranges == 0:
            return 0
            
        minutes = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Step 2: Multi-source BFS layer by layer
        while q and fresh_oranges > 0:
            minutes += 1
            # Process all rotten oranges currently at this minute's level
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # If neighbor is a fresh orange, it becomes rotten
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr, nc))
                        
        # Step 3: If fresh oranges remain, they are isolated; return -1
        return minutes if fresh_oranges == 0 else -1