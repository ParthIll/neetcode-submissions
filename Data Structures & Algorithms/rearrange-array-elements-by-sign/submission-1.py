class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for num in nums:
            if num<=0:
                neg.insert(0,num)
            else:
                pos.insert(0,num)
        ret=[]
        for i in range(len(nums)//2):
            ret.append(pos.pop())
            ret.append(neg.pop())
        return ret