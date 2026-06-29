class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subsets = [[]]
        for i in range(len(nums)):
            
            for subset in subsets:
                print(i)
                res.append(subset+[nums[i]])
            subsets=res.copy()
            print(res)
        return res