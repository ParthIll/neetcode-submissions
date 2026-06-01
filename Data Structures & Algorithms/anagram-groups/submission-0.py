from collections import defaultdict
from typing import List
class Solution:
    def checkAnagram(self,s:str,t:str) ->bool:
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = [[strs[0]]]
        i=0
        while i<len(strs):
            j=i+1
            while j<len(strs):
                if self.checkAnagram(strs[i],strs[j]):
                    ret[i].append(strs[j])
                    strs.pop(j)
                    j-=1
                j+=1
            i+=1
            if(i<len(strs)):
                ret.append([strs[i]])
        return ret
                
                    
            
        
