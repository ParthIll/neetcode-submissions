class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num=n
        while num!=1:
            if num in seen:
                return False
            seen.add(num)
            adder=0
            while num>0:
                adder+=(num%10)**2
                num//=10
                
            num=adder
            

        return True