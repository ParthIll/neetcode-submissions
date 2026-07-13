class Solution:
    def canJump(self, nums: List[int]) -> bool:
        q=deque()
        q.append(len(nums)-1)
        dp=set()
        while q:
            x=q.popleft()
            if x==0:
                return True
            if x in dp:
                continue
            dp.add(x)
            for i in range(x-1,-1,-1):
                if nums[i]>=x-i:
                    q.append(i)
            



        return False