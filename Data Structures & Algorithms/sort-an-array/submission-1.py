class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ret=[]
        heapq.heapify(nums)
        while nums:
            ret.append(heapq.heappop(nums))
        return ret