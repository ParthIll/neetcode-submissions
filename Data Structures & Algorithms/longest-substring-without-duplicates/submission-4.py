class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longLen = 0
        l=0
        r=0
        curMap=defaultdict(int)
        while r<len(s):
            cur = s[r]
            if curMap[cur]==0:
                curMap[cur]=1
                r+=1;   
            else:
                while True:
                    if s[l] == cur:
                        l+=1
                        curMap[cur]-=1
                        break
                    curMap[s[l]]-=1
                    l+=1
            longLen = max(longLen,r-l)
        return longLen

