class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft =[0]*len(height)
        maxright = [0]*len(height)
        maxheight = 0
        for i in range(len(height)):
            maxheight = max(maxheight, height[i])
            maxleft[i] = maxheight
        maxheight =0
        for i in range(len(height)-1,-1,-1):
            maxheight = max(maxheight, height[i])
            maxright[i] = maxheight
        water= 0 

        for i in range(len(height)):
            if min(maxleft[i],maxright[i])-height[i]>0:
                water+=min(maxleft[i],maxright[i])-height[i]
            
        return water