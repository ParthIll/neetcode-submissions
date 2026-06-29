class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            heapq.heappush(min_heap,(((point[0])**2+(point[1])**2)**0.5,point))
        ret =[]
        for i in range(k):
            ret.append(heapq.heappop(min_heap)[1])
        return ret