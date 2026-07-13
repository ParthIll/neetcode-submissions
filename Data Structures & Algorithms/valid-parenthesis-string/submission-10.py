class Solution:
    def checkValidString(self, s: str) -> bool:
        cMin = 0  # Minimum possible open '('
        cMax = 0  # Maximum possible open '('
        
        for c in s:
            if c == "(":
                cMin += 1
                cMax += 1
            elif c == ")":
                cMin -= 1
                cMax -= 1
            else:  # c == '*'
                cMin -= 1  # If '*' acts as ')'
                cMax += 1  # If '*' acts as '('
            
            # If cMax drops below 0, it means we have too many ')' and not even 
            # turning every single '*' into '(' can save it.
            if cMax < 0:
                return False
                
            # cMin can never drop below 0 because we can't have "negative" open parentheses.
            # If it goes negative, it just means we chose to turn too many '*' into ')'.
            # We reset it to 0 (meaning we treat those excess '*' as empty strings instead).
            if cMin < 0:
                cMin = 0
        
        # If cMin is 0, it means it's possible to perfectly balance all parentheses.
        return cMin == 0