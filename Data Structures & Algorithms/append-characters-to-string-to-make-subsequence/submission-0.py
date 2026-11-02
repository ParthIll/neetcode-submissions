class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        charsNeeded = len(t)
        cur = 0
        for i in range(len(s)):
            if(s[i]==t[cur]):
                cur+=1
                charsNeeded-=1
            if(cur>=len(t)):
                return 0

        return charsNeeded