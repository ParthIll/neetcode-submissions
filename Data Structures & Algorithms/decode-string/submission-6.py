class Solution:
    def decodeString(self, s: str) -> str:
        visited=set()
        def dfs(i):
            ret=""
            for j in range(i,len(s)):
                
                if j not in visited:
                    visited.add(j)
                    if s[j] =="[":
                        continue
                    if s[j] in "abcdefghijklmnopqrstuvwxyz":
                        ret+=s[j]
                    elif s[j]=="]":
                        break
                    else:
                        num=0
                        x=j
                        while s[x] in "0123456789":
                            visited.add(x)
                            num=int(s[j:x+1])
                            x+=1
                        ret+=num*dfs(x+1)
            return ret

        return dfs(0)
        