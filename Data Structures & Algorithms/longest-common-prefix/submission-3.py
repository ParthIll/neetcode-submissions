class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=list(strs[0])
        if "" in strs:
            return ""
        for st in strs:
            s=s[:len(st)]
            for i in range(len(st)-1,-1,-1):
                if i not in range(len(s)):
                    
                    continue
                elif s[i]!=st[i]:
                    s=s[0:i]
        return "".join(s)