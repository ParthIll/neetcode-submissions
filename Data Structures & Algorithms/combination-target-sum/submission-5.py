class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [[]]
        result = []
        for i in range(len(nums)):
            ress=res.copy()
            for subset in ress:
                num=[nums[i]]
                while sum(num+subset)<=target:

                    
                    res.append(subset+num)
                    num.append(nums[i])
        for sub in res:
            if sum(sub)==target:
                result.append(sub)
        return result