class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res =[]
        for l,r in queries:
            numWords = 0
            for i in range(l,r+1):
                if(words[i][0] in "aeiou" and words[i][-1] in "aeiou"):
                    numWords+=1

            res.append(numWords)
        return res