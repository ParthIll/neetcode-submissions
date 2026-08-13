class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        word_map = {}
        word_map = defaultdict(int)
        for j in range(len(s)):
            word_map[s[j]]+=1
        for i in range(len(t)):
            if t[i] in word_map:
                if word_map.get(t[i]) == 1:
                    del word_map[t[i]]
                else:
                    word_map[t[i]]-=1

            else:
                return False
            
        return len(word_map)==0
