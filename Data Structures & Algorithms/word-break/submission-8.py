from collections import deque
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert to a set for O(1) lookups
        word_set = set(wordDict)
        
        # Queue stores the starting index of the substring we want to match
        q = deque([0])
        
        # Visited set tracks indices we've already processed to avoid duplicate work
        visited = {0}
        
        while q:
            start = q.popleft()
            
            # If our starting index reaches the end of the string, we successfully broke the word!
            if start == len(s):
                return True
                
            # Try every possible ending index for the current substring
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is a valid word, the next start position is 'end'
                if substring in word_set:
                    if end not in visited:
                        visited.add(end)
                        q.append(end)
                        
        return False