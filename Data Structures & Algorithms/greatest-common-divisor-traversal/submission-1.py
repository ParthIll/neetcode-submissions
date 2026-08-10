import math
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        finished = set()
        combs=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                combs.append([i,j])
        visit=set()
        def bfs (start,end):
            if start in visit:
                return False
            visit.add(start)
            if (start,end) in finished:
                return True
            if math.gcd(nums[start],nums[end])>1:
                finished.add((start,end))
                return True
            else:
                for i in range(len(nums)):
                    if i!= start and math.gcd(nums[start],nums[i])>1:
                        finished.add((start,i))
                        if bfs(i,end):
                            return True
            return False
        for comb in combs:
            visit=set()
            if not bfs(comb[0],comb[1]):
                return False
        return True
