class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        self.visited=set()
        self.clear= False
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols):
                self.clear=True
                return
            if (r,c) in self.visited or board[r][c] =="X":
                return
            self.visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    dfs(r,c)
                    if not self.clear:
                        for dr,dc in self.visited:
                            board[dr][dc] ="X"
                    self.visited = set()
                    self.clear=False
        
            