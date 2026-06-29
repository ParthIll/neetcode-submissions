class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # Pops the smallest, keeping only the largest k elements
                
        return min_heap[0] # The root is the kth largest