class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dic = set(dictionary)
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]

            # Option 1: Skip s[i] as an extra character
            ans = 1 + dfs(i + 1)

            # Option 2: Try to match a word starting at index i
            for j in range(i + 1, n + 1):
                if s[i:j] in dic:
                    ans = min(ans, dfs(j))

            memo[i] = ans
            return ans

        return dfs(0)