class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: if there are fewer than 2 days, no profit can be made
        if not prices or len(prices) < 2:
            return 0
        
        min_price = float('inf')  # Start with the highest possible value
        max_profit = 0            # Start with 0 profit
        
        for price in prices:
            # Update the lowest price we've seen so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if we sold today, and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit