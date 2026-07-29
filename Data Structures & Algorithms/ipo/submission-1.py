class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profCap = [(cap,pro)for pro,cap in zip(profits,capital)]
        profCap.sort()
        profits = [pro for cap,pro in profCap]
        capital = [cap for cap,pro in profCap]
        cur=w
        x=0
        ranges=[]
        for i in range(k):
            
            while x<len(capital) and capital[x]<=cur:
                ranges.append((profits[x]))
                x+=1
            if not ranges:
                return cur
            cur+=max(ranges)
            ranges.pop(ranges.index(max(ranges)))
            

        return cur