class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp=defaultdict(int)
        for x in nums:
            dp[(x,)]=x
        nums.insert(0,1)
        nums.append(1)
        def foo(arr):
            if not arr or arr==[1,1] or arr==[1]:
                return 0
            if tuple(arr) in dp:
                return dp[tuple(arr)]
            maxdp=0
            
            for i in range(1,len(arr)-1):
                mult=1
                mult*=arr[i]*arr[i-1]*arr[i+1]
                maxdp=max(maxdp,foo(arr[:i]+arr[i+1:])+mult)
            dp[tuple(arr)] = maxdp
            return dp[tuple(arr)]

        
        return foo(nums)
