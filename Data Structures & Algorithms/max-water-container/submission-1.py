class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxim = j*(min(heights[j],heights[i]))
        while(i<j):
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
            maxim=max(maxim,(j-i)*min(heights[j],heights[i]))
        return maxim