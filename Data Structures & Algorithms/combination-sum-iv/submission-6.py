class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ways = defaultdict(int)
        ways[0]=1
        for i in range(target+1):
            for n in nums:
                if i-n>=0:
            
                    ways[i]+=ways[i-n]
            
        return ways[target]