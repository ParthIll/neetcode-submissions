
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        mx = n
        mn=1
        while True:
            g=(mn+mx)//2
            res=guess(g)
            if res==0:
                return g
            elif res==-1:
                mx=g-1
            else:
                mn=g+1
        
                
