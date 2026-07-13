class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q=[]
        q.append(len(nums)-1)
       
        while q:
            x=q.pop()
            if x==0:
                return True
            
            
            for i in range(x-1,-1,-1):
                if nums[i]>=x-i:
                    q.append(i)
            



        return False