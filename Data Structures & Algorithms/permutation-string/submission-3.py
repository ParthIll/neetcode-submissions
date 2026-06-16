class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1map = {}
        s2map = {}
        
        # 1. Build the target map (s1) and the first window map (s2)
        for i in range(len(s1)):
            s1map[s1[i]] = s1map.get(s1[i], 0) + 1
            s2map[s2[i]] = s2map.get(s2[i], 0) + 1
            
        # If the first window happens to be a match, we're done!
        if s1map == s2map:
            return True
            
        # 2. Slide the window character by character
        l = 0
        for r in range(len(s1), len(s2)):
            # Bring the new right character into the window
            s2map[s2[r]] = s2map.get(s2[r], 0) + 1
            
            # Drop the old left character out of the window
            s2map[s2[l]] -= 1
            if s2map[s2[l]] == 0:
                del s2map[s2[l]]  # Clean up keys with 0 count so dict comparison works
                
            l += 1
            
            # Check the *entire* window state at once
            if s1map == s2map:
                return True
                
        return False