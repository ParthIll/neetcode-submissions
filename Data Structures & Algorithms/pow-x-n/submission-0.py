class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        orig=x
        if n>0:
            for i in range(n-1):
                x*=orig
        elif n==0:
            return 1
        else:
            n=-1*n
            for i in range(n-1):
                x*=orig
            x=1/x
            
        return x