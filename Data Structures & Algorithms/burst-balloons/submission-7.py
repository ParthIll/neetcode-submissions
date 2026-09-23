class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        cache = {}
        for num in nums:
            cache[tuple([num])] = num
        
        
        def foo(nums):
            if tuple(nums) in cache:
                return cache[tuple(nums)]
            maxVal = 0
            for i in range(1,len(nums)-1):
                maxVal = max(maxVal,nums[i]*nums[i-1]*nums[i+1]+foo(nums[:i]+nums[i+1:]))
            cache[tuple(nums)]=maxVal
            return maxVal
        
        
        
        x = foo(nums)
        return x