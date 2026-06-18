class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid=len(nums)//2
        if target ==nums[-1]:
            return len(nums)-1
        if target == nums[0]:
            return 0
        iterations =0
        print(mid)
        while True:
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                mid=mid//2
            else:
                mid = mid + max(mid//2,1)
                if mid > len(nums)-1:
                    return -1
                
            iterations+=1
            if iterations > len(nums):
                return -1