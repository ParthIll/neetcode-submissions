class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret=[]
        def recur(matrix):
            if not matrix:
                return
            if len(matrix)<2:
                for r in matrix[0]:
                    ret.append(r)
                return
            if len(matrix[0])<2:
                for r in matrix:
                    try:
                        ret.append(r[0])
                    except:
                        continue
                return
            top = [matrix[0][i] for i in range(len(matrix[0]))]
            right = [matrix[i][-1] for i in range(len(matrix))]
            bottom = [matrix[-1][i] for i in range(len(matrix[-1])-1,-1,-1)]
            left = [matrix[i][0] for i in range(len(matrix)-1,-1,-1)]
            for t in top:
                ret.append(t)
            for r in right[1:]:
                ret.append(r)
            for b in bottom[1:]:
                ret.append(b )
            for l in left[1:-1]:
                ret.append(l)
            inner =[row[1:-1] for row in matrix[1:-1]]

            print("top",top)
            print("right",right)
            print("bottom",bottom)
            print("left",left)
            recur(inner)
        recur(matrix)
        return ret