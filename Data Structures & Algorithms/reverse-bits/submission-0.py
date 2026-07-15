class Solution:
    def reverseBits(self, n: int) -> int:
        exp=31
        ret=0
        while n>0:
            if n>=2**exp:
                n-=2**exp
                ret+=2**(31-exp)
            exp-=1
        return ret