class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache={}
        def foo(ind,canBuy):
            
            if(ind==len(prices)):
                return 0
            if (ind,canBuy) in cache:
                return cache[(ind,canBuy)]
            elif(canBuy):
                cache[(ind,canBuy)] = max(foo(ind+1,canBuy),foo(ind+1,not canBuy)-prices[ind])
                return cache[(ind,canBuy)]
            else:
                cache[(ind,canBuy)] = max(foo(ind+1,canBuy),foo(ind+1,not canBuy)+prices[ind])
                return cache[(ind,canBuy)]
        return foo(0, True)
        