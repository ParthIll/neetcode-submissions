from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def dfs(r, c, visited, prev_height):
            # 1. Check out of bounds, already visited, or if it flows downhill toward land (invalid for reverse tracking)
            if (r not in range(rows) or 
                c not in range(cols) or 
                (r, c) in visited or 
                heights[r][c] < prev_height):
                return
                
            # 2. Mark this cell as able to reach the respective ocean
            visited.add((r, c))
            
            # 3. Move to neighbors (water flows to equal or higher ground in reverse)
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Step 1: Start DFS from the top/bottom rows (horizontal borders)
        for c in range(cols):
            dfs(0, c, pacific_visited, heights[0][c])                # Top row -> Pacific
            dfs(rows - 1, c, atlantic_visited, heights[rows - 1][c])  # Bottom row -> Atlantic

        # Step 2: Start DFS from the left/right columns (vertical borders)
        for r in range(rows):
            dfs(r, 0, pacific_visited, heights[r][0])                # Left col -> Pacific
            dfs(r, cols - 1, atlantic_visited, heights[r][cols - 1])  # Right col -> Atlantic

        # Step 3: Find cells that are present in BOTH sets
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_visited and (r, c) in atlantic_visited:
                    result.append([r, c])
                    
        return result