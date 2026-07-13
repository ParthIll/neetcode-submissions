class Solution:
    def jump(self, nums: List[int]) -> int:
        q=deque()
        q.append((len(nums)-1,0))
       
        while q:
            x,r=q.popleft()
            if x==0:
                return r
            
            
            for i in range(x-1,-1,-1):
                if nums[i]>=x-i:
                    q.appendleft((i,r+1))
            



        return -1