class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        def calc(h1,h2):
            return min(heights[h1],heights[h2])*(h2-h1)
        maxVal = calc(l,r)
        while l<r:
            maxVal = max(maxVal,calc(l,r))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxVal
