import re
class Solution:
    def simplifyPath(self, path: str) -> str:
        ret=""
        splt=re.split(r"/+", path)
        splt=list(filter(None, splt))
        stack=[]
        for st in splt:
            if st in "..":
                if st==".":
                    continue
                else:
                    if stack:
                        stack.pop()
                
            else:
                stack.append(st)
        
        return "/"+"/".join(stack)