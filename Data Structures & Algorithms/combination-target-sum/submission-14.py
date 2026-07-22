class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]  # Base case: 1 way to make sum 0 (empty list)

        for num in nums:
            for i in range(num, target + 1):
                for combination in dp[i - num]:
                    dp[i].append(combination + [num])

        return dp[target]