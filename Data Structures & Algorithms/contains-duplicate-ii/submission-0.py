class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        iMap={}
        for i in range(len(nums)):
            if nums[i] in iMap and abs(iMap[nums[i]]-i)<=k:
                return True
            iMap[nums[i]]=i
        return False