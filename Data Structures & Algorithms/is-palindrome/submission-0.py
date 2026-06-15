class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text)
        print(cleaned)
        if "".join(reversed(cleaned)) == (cleaned):
            return True
        else:
            return False