class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ret=[]
        words = set(wordDict)
        def dfs(i,cur):
            if i==len(s):
                if cur[-1] in words:
                    ret.append(" ".join(cur))
                    return
                else:
                    return
            if cur[-1] not in words:
                cur[-1]+=s[i]
                dfs(i+1,cur)
            else:
                op1=cur.copy()
                op1.append(s[i])
                dfs(i+1,op1)
                op2 = cur.copy()
                op2[-1]+=s[i]
                dfs(i+1,op2)

            

        dfs(0,[""])
        return ret