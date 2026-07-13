from collections import deque

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        words = set()
        q = deque()
        w1list = list(word1)
        q.append((w1list, 0, 0))
        
        while q:
            s, x, z = q.popleft()
            
            if ("".join(s), x) in words:
                continue
            words.add(("".join(s), x))
            
            if "".join(s) == word2:
                return z
            
            if x >= len(word2):
                if len(s) > len(word2):
                    delcopy = s.copy()
                    del delcopy[-1] 
                    q.append((delcopy, x, z + 1))
                continue
            
            if x >= len(s):
                y = word2[x]
                incopy = s.copy()
                incopy.append(y)
                q.append((incopy, x + 1, z + 1))
                continue
            
            if s[x] == word2[x]:
                # FIX: Cost is 0, so prioritize this state by putting it at the front!
                q.appendleft((s, x + 1, z))
                continue
            else:
                incopy = s.copy()
                delcopy = s.copy()
                repcopy = s.copy()
                y = word2[x]
                
                incopy.insert(x, y)
                q.append((incopy, x + 1, z + 1))
                
                del delcopy[x]
                q.append((delcopy, x, z + 1))
                
                repcopy[x] = y
                q.append((repcopy, x + 1, z + 1))
        
        return 0