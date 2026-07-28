class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if i+1 not in range(len(nums)) or nums[i+1]!=nums[i]:
                return nums[i]
            i+=2