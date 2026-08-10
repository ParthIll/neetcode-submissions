class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [1]*(n+1)
        trib[0]=0
        for i in range(3,n+1):
            trib[i]=trib[i-1]+trib[i-2]+trib[i-3]
        return trib[n]