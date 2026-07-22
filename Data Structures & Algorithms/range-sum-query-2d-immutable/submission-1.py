class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        ROWS=len(matrix)
        COLS = len(matrix[0])
        self.sums =[[0]*COLS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.sums[r][c]=matrix[r][c]
                if r-1 in range(ROWS):
                    self.sums[r][c]+=sum(matrix[x][c] for x in range(r))
                if c-1 in range(COLS):
                    self.sums[r][c]+=self.sums[r][c-1]
        print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret= self.sums[row2][col2]
        if row1-1 in range(len(self.matrix)):
            ret-=self.sums[row1-1][col2]
        if col1-1 in range(len(self.matrix[0])):
            ret-=self.sums[row2][col1-1]
            if row1-1 in range(len(self.matrix)):
                ret+=self.sums[row1-1][col1-1]
        return ret
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)