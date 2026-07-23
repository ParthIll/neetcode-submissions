class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ret=""
        for i in range(min(len(word1),len(word2))):
            ret+=word1[i]
            ret+=word2[i]
        if len(word1)>len(word2):
            ret+=word1[len(word2):]
        elif len(word2)>len(word1):
            ret+= word2[len(word1):]
        return ret