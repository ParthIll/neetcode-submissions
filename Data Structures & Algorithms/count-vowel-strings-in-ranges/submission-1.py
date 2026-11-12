class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
     
        for i in range(len(words)):
            prefix[i + 1] = prefix[i]
            if words[i][len(words[i])-1] in vowels and words[i][0] in vowels:
                prefix[i + 1] += 1
                #if i == len(words) - 1:
                    #prefix[i+1] = prefix[i] + 1
        ans = []
        print(prefix)
        for i in range(len(queries)):
            ans.append(prefix[queries[i][1]+1] - prefix[queries[i][0]])
         
        return ans