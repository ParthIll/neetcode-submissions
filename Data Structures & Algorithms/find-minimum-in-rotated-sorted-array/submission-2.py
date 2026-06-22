class Solution:
    def findMin(self, nums: List[int]) -> int:
        left  =0
        right = len(nums)-1
        mid = (left+right)//2
        if nums[left]<nums[right]:
            return nums[left]
        if right==1:
            return min(nums[right],nums[left])
        if nums[mid]>nums[left]:
            left=mid+1
        else:
            right =mid
        while(left!=right):
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right =mid
        return nums[left]
