class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax=nums[0]
        globmin=nums[0]
        curmin=0
        curmax=0
        for i in range(len(nums)):
            curmin=min(curmin+nums[i],nums[i])
            curmax=max(curmax+nums[i],nums[i])
            globmin=min(globmin,curmin)
            globmax=max(globmax,curmax)
        if globmin==sum(nums):
            return globmax
        return max(globmax,sum(nums)-globmin)