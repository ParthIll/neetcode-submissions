class Solution:
    def rob(self, nums: List[int]) -> int:
        numms=list(nums)
        numms.append(0)
        numms.append(0)
        numms.append(0)
        for i in range(len(numms)-4,-1,-1):
            numms[i]=numms[i]+max(numms[i+2],numms[i+3])
        return max(numms[0],numms[1])