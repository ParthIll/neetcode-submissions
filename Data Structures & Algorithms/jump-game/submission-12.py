class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q=deque()
        q.append(len(nums)-1)
       
        while q:
            x=q.popleft()
            if x==0:
                return True
            
            
            for i in range(x-1,-1,-1):
                if nums[i]>=x-i:
                    q.appendleft(i)
            



        return False