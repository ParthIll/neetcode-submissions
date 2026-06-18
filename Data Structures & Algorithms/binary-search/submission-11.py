class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target ==nums[-1]:
            return len(nums)-1
        if target == nums[0]:
            return 0
        l=0
        r=len(nums)-1
        while l <=r:
            mid=r-l//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return -1
        