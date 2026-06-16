from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
            try:
                stack = deque()
            
                parenth ={'}':'{',
                ']':'[',')':'('}
                for c in s:
                    if c in parenth.values():
                        stack.append(c)
                    
                    elif parenth[c] == stack.pop():
                        continue
                    else:
                        return False
                if len(stack)==0:
                    return True
                else:
                    return False
            except:
                return False
