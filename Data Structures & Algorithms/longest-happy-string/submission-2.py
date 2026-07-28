class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        a,b,c=min(((b+c)*2)+2,a),min(((a+c)*2)+2,b),min(((b+a)*2)+2,c)
        ret=""
        heap=[(-a,"a"),(-b,"b"),(-c,"c")]
        heapq.heapify(heap)
        while heap:
            
            x,c = heapq.heappop(heap)
            if x==0:
                continue
            if len(ret)>=2 and  c==ret[-1] and c==ret[-2]:
                nextx,nextc = heapq.heappop(heap)
                ret+=nextc
                heapq.heappush(heap,(x,c))
                heapq.heappush(heap,(nextx+1,nextc))
                continue
            ret+=c
            if x+1!=0:
                heapq.heappush(heap,(x+1,c))
        return ret