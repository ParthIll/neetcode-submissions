class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        exp=31
        while n>0:
            if n>=2**exp:
                n-=2**exp
                ones+=1
            exp-=1
        return ones