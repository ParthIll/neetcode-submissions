class Solution:
    def reverse(self, x: int) -> int:
        neg=False
        if x<0:
            neg=True
        x=abs(x)
        stack=[]
        while x!=0:
            stack.append(x%10)
            x//=10
        exp=0
        ret=0
        while stack:
            ret+=stack.pop()*(10**exp)
            exp+=1
        if abs(ret>>1)>2**30:
            return 0
        else:
            return ret if not neg else ret*-1
        