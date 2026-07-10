class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tMap={}
        tMap[target]=1
        for i in range(len(nums)):
            num=nums[i]
            tCopy={}
            for t in tMap:
                tCopy[t+num]=tCopy.get(t+num,0)+tMap[t]
                tCopy[t-num]=tCopy.get(t-num,0)+tMap[t]
            tMap=tCopy
            print(tMap)


        return tMap.get(0,0)