import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        maxim = math.ceil((max(piles)/h)*len(piles))
        minim = math.ceil(min(piles)/h*len(piles))
        minK=1000000000000000000000
        while minim<=maxim:
            mid = (minim+maxim)//2
            hourcount=h
            for pile in piles:
                hourcount-=math.ceil(pile/mid)
            if hourcount >=0:
                minK = min(minK,mid)
                maxim = mid-1
            else:
                minim = mid+1
        return minK
