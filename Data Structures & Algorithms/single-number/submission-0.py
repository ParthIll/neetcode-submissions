class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] not in nums[:i]+nums[i+1:]:
                return nums[i]
        return 0