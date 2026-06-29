class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneheap = []
        for stone in stones:
            heapq.heappush(stoneheap,-1*stone)
        while len(stoneheap)>1:
            print(stoneheap)
            y=-1*heapq.heappop(stoneheap)
            x=-1*heapq.heappop(stoneheap)
            if x!=y:
                heapq.heappush(stoneheap,-1*(y-x))
                continue
        try:
            return -1*stoneheap[0]
        except:
            return 0