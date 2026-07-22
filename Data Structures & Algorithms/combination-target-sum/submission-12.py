class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        q=deque()
        for num in nums:
            q.append(([num],num))
        res=[]
        visited=set()
        while q:
            
            x,summ=q.popleft()
            
            
            if summ==target:
                res.append(x.copy())
                continue
            for i in range(nums.index(x[-1]),len(nums)):
                num=nums[i]
                if summ+num<target:
                    xcopy=x.copy()
                    xcopy.append(num)
                    
                    q.append((xcopy,summ+num))
                elif summ+num==target:
                    xcopy=x.copy()
                    xcopy.append(num)
                    
                    res.append(xcopy)
        return res
            
            