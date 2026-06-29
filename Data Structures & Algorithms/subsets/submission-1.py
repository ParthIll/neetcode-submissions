class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subsets = [[]]
        for i in range(len(nums)):
            ress=res.copy()
            for subset in ress:
                
                res.append(subset+[nums[i]])
            
        return res