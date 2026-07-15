class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        exp=0
        for i in range(len(digits)-1,-1,-1):
            num+=digits[i]*(10**exp)
            exp+=1

        num = num+1
        ret=[]
        while num!=0:
            ret.insert(0,num%10)
            num//=10
        return ret