class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        maxim = height[0]
        for i in range(1,len(height)):
            if height[i]>maxim:
                maxim=height[i]
            leftMax[i]=maxim
        rightMax[-1]=height[-1]
        maxim=rightMax[-1]
        for i in range(len(height)-2,-1,-1):
            if height[i]>maxim:
                maxim=height[i]
            rightMax[i]=maxim
        ret = 0
        print(leftMax)
        print(rightMax)
        for i in range(1,n-1):
            if height[i]<min(leftMax[i],rightMax[i]):
                ret+=min(leftMax[i],rightMax[i])-height[i]

        return ret