import math
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canWork(cap):
            groups =k-1
            curSum=0
            for n in nums:
                if curSum+n<=cap:
                    curSum+=n
                else:
                    curSum=n
                    groups-=1
            
            if groups>=0:
                return True
            return False
        l=max(nums)
        r=sum(nums)
        if canWork(l):
            return l
        res=0
        while l<=r:
            m=(l+r)//2
            if canWork(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res
