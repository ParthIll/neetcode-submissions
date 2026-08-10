class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rows=[]
        cols=[]
        rowConditions.sort()
        colConditions.sort()
        rows=defaultdict(set)
        cols=defaultdict(set)
        for i in range(k):
            for ab,bel in rowConditions:
                rows[ab].add(bel)
                rows[ab]|=rows[bel]
                if ab in rows[ab] or ab in rows[bel]:
                    return[]
        
        rows = dict(sorted(rows.items(),key =lambda x:len(x[1]),reverse=True))
        row=[]
        for r in rows:
            row.append(r)
        for i in range(1,k+1):
            if i not in row:
                row.append(i)

        for i in range(k):
            for ab,bel in colConditions:
                cols[ab].add(bel)
                cols[ab]|=cols[bel]
                if ab in cols[ab] or ab in cols[bel]:
                    return[]
        
        cols = dict(sorted(cols.items(),key =lambda x:len(x[1]),reverse=True))
        col=[]
        for r in cols:
            col.append(r)
        for i in range(1,k+1):
            if i not in col:
                col.append(i)
        print(rows)
        print(row)
        print(cols)
        print(col)
        matr=[[0]*k for _ in range(k)]
        for i,r in enumerate(row):
            matr[i][col.index(r)]=r
        return matr

