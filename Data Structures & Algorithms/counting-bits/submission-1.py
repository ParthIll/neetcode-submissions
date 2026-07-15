class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[]
        while n>=0:
            ret.insert(0,bin(n).count('1'))
            n-=1
        return ret