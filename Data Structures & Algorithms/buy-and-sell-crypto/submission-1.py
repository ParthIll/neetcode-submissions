class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxright = [0]*len(prices)
        maxprof = [0]*len(prices)
        maxVal = prices[-1]
        for i in range(len(prices)-1,-1,-1):
            maxprof[i]=maxVal-prices[i]
            maxVal = max(maxVal,prices[i])
        
        return max(maxprof)