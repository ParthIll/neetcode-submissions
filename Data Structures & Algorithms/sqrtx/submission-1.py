class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(2**16):
            if i*i>x:
                return i-1