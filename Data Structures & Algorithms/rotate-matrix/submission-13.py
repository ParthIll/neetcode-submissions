class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = [matrix[i][0] for i in range(len(matrix)-1,-1,-1)]
        top = [matrix[0][i] for i in range(len(matrix[0]))]
        right = [matrix[i][-1] for i in range(len(matrix)-1,-1,-1)]
        bottom = [matrix[-1][i] for i in range(len(matrix[-1]))]
        print("left",left)
        print("top",top)
        print("right",right)
        print("bottom",bottom)
        for i in range(len(left)):
            matrix[0][i]=left[i]
        for i in range(len(top)):
            matrix[i][-1] = top[i]
        for i in range(len(right)):
            matrix[-1][i] = right[i]
        for i in range(len(bottom)):
            matrix[i][0]=bottom[i]
        if len(top)>=4:
            
            inner = [row[1:-1] for row in matrix[1:-1]]
            print(inner)
            self.rotate(inner)
            print(inner)
            for i in range(len(matrix[1:-1])):
                row = matrix[i+1]
                row[1:-1] = inner[i]
            print(matrix)
            