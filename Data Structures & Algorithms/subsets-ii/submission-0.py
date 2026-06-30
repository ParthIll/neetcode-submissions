class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        retset = set()
        for num in nums:
            for i in range(len(res)):
                probe = res[i]+[num]
                if tuple(probe) not in retset:
                    res.append(probe)
                    retset.add(tuple(probe))
        return res

