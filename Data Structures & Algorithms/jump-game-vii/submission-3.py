class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        memo={}
        def dfs(ind):
            if ind in memo:
                return memo[ind]
            if ind==len(s)-1:
                return True
            for add in range(maxJump,minJump-1,-1):
                if ind+add in range(len(s)) and s[ind+add]=="0" and dfs(ind+add):
                    memo[ind]=True
                    return True
            memo[ind]=False
            return False

        ans= dfs(0)
        print(memo)
        return ans