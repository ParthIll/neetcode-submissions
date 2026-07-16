class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        output=[]
        cset={}
        for i in range(len(words)-1):
            if words[i+1] in words[i] and len(words[i])>len(words[i+1]):
                return ""
            for c1,c2 in zip(words[i],words[i+1]):
                
                if c1==c2:
                    if c1 not in cset:
                        cset[c1]=[]
                        
                else:
                    if c1 in cset and c2 in cset:
                        if c2 in cset[c1]:
                            return""
                    if c2 not in cset:
                        cset[c2]=[c1]
                    else:
                        if c1 not in cset[c2]:
                            cset[c2].append(c1)
                    break
        print(cset)
        visited=set()
        def dfs(char):
            if char in visited:
                return False
            visited.add(char)
            
            if char not in cset or cset[char]==[]:
                if char not in output:
                    output.append(char)
            else:
                
                for c in cset[char]:
                    dfs(c)
                    if char in output and output.index(char)<output.index(c):
                        return False
                if char not in output:
                    output.append(char)
            return True          
        for char in cset:
            visited=set()
            if not dfs(char):
                return ""
        for word in words:
            for c in word:
                if c not in output:
                    output.append(c)
                    cset[c]=[]

        
        return "".join(output)