class Solution:
    def numSquares(self, n: int) -> int:
        nums=[]
        for i in range(1,n+1):
            if i*i>n:
                break
            else:
                nums.append(i*i)
        ways = [-1]*(n+1)
        ways[0]=0
        for i in range(n+1):
            for nu in nums:
                if i-nu>=0 and ways[i-nu]!=-1:
                    if ways[i]==-1:
                        ways[i]=ways[i-nu]+1
                    else:
                        ways[i]=min(ways[i],ways[i-nu]+1)
        
        
        return ways[n]
         