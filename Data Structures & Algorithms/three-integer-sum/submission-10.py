
class Solution:
    def twoSum(self,nums:List[int],target):
        nums.sort()
        found = []
        check =set()
        prev=nums[0]
        for x in nums:
            
            
            if target-x in check:
                found.append([target-x,x])
            check.add(x)
        return found
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        visited=set()
        for i in range(len(nums)):
            z = nums[i]
            pairs = self.twoSum(nums[:i]+nums[i+1:],0-z)
            for x,y in pairs:
                if(tuple(sorted((x,y,z))) not in visited):
                    visited.add(tuple(sorted((x,y,z))))
                    ret.append([x,y,z])
        return ret
        
