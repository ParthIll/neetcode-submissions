class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i=0
        l=len(nums)
        nCount=Counter(nums)
        for k in nCount:
            if nCount[k]>4:
                for i in range(nCount[k]-4):
                    nums.remove(k)
        
        def dfs(nums,amount,target):
            ret=[]
            visited=set()
            
            if amount==0:
                if target==0:
                    return[[]]
                else:
                    return []
            
            
            
            for i in range(len(nums)):
                
                for arr in dfs(nums[i+1:],amount-1,target-nums[i]):
                    add=[nums[i]]
                    add+=arr
                    if amount==4 and tuple(add)  in visited:
                        continue
                    ret.append(add)
                    visited.add(tuple(add))
            
            return ret

        return dfs(nums,4,target)
