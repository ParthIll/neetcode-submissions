class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        listSet = {}
        for cand in candidates:
            listSet[cand] = listSet.get(cand,0)+1
        dupe = listSet.copy()
        candidates.sort()
        nums = candidates
        res = [[]]
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            ress=res.copy()
            for subset in ress:
                
                num=[nums[i]]
                while sum(num+subset)<=target and listSet[nums[i]]>0:

                    listSet[nums[i]]-=1
                    res.append(subset+num)
                    num.append(nums[i])

                listSet = dupe.copy()
        for sub in res:
            if sum(sub)==target:
                result.append(sub)
        return result