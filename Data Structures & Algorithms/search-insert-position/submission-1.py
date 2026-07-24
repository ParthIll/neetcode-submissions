class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        m=(r+l)//2
        while l<=r:
            
            if nums[m]==target:
                return m
            if nums[m]<target:
                l=m+1
            else:
                r=m-1

            m=(r+l)//2
            
        return l