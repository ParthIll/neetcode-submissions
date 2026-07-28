import math
class Solution:
    def reorganizeString(self, s: str) -> str:
        cCount = defaultdict(int)
        for c in s:
            cCount[c]-=1

        if abs(min(cCount.values()))>math.ceil(len(s)/2):
            return ""
        ret=""
        items = [tuple(reversed(item)) for item in cCount.items()]
        heapq.heapify(items)
        
        while items:
            print(items)
            x,c = heapq.heappop(items)
            if not items:
                ret+=str(c)
                return ret
            nextx,nextc = heapq.heappop(items)
            ret+=str(c)
            ret+=str(nextc)
            if x+1!=0:
                heapq.heappush(items,(x+1,c))
            if nextx+1!=0:
                heapq.heappush(items,(nextx+1,nextc))
        return ret
