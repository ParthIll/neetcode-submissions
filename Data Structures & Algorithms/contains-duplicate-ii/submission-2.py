class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for x in range(len(nums)-1):
            for i in range(x+1,min(len(nums),x+k+1)):
                if nums[x]==nums[i]:
                    return True
        return False