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
        r=l*(math.ceil(len(nums)/k))
        if canWork(l):
            return l
        for i in range(l,r+1):
            if canWork(i):
                return i
