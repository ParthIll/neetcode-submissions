class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        matrix.insert(0,[0]*(len(matrix[0])+1))
        for r in range(1,len(matrix)):
            matrix[r].insert(0,0)
        ROWS=len(matrix)
        COLS = len(matrix[0])
        self.sums =[[0]*COLS for _ in range(ROWS)]
        for r in range(1,ROWS):
            for c in range(1,COLS):
                self.sums[r][c]=matrix[r][c]
                
                
                inner = self.sums[r-1][c-1]
                self.sums[r][c]+=(self.sums[r-1][c])+(self.sums[r][c-1]-inner)
        matrix.pop(0)
        for r in range(len(matrix)):
            matrix[r].pop(0)
        self.sums.pop(0)
        for r in range(len(self.sums)):
            self.sums[r].pop(0)
        self.matrix=matrix
        print(self.sums)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ret= self.sums[row2][col2]
        if row1-1 >=0:
            ret-=self.sums[row1-1][col2]
        if col1-1 >=0:
            ret-=self.sums[row2][col1-1]
            if row1-1>=0:
                ret+=self.sums[row1-1][col1-1]
        return ret
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)