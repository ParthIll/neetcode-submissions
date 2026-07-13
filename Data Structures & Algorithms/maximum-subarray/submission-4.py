class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum=0
        sumleft=[0]*len(nums)
        sumRight = [0]*len(nums)
        for i in range(len(nums)):
            curSum+=nums[i]
            sumleft[i]=curSum
        curSum=0
        for i in range(len(nums)-1,-1,-1):
            curSum+=nums[i]
            sumRight[i]=curSum
        
        l=sumRight.index(max(sumRight))
        r=sumleft.index(max(sumleft))
        if l>r:
            return max(nums)
        print(l,r)
        print(sumleft,sumRight)
        return sum(nums[l:r+1])
