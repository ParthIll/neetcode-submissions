class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listmap = {}
        for i in range(len(nums)):
            x= target - nums[i]
            if x in listmap:
                return [listmap[x],i]
            listmap[nums[i]] = i