class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board = [["."]*n for i in range(n)]
        def dfs(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if self.isSafe(r,c,board):
                    board[r][c] = "Q"
                    dfs(r+1)
                    board[r][c]="."
        dfs(0)
        return res
    def isSafe(self,r,c,board):
        if r==0:
            return True
        Qlist = []
        rows,cols = len(board),len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] =="Q":
                    Qlist.append((row,col))
        for tup in Qlist:
            if r == tup[0] or c == tup[1] or abs(r-tup[0])==abs(c-tup[1]):
                return False
        return True