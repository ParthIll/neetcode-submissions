class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ret=""
        j=0
        for i in range(min(len(word1),len(word2))):
            ret+=word1[i]
            ret+=word2[i]
            j=i
        
        ret+=word1[j+1:]
    
        ret+= word2[j+1:]
        return ret