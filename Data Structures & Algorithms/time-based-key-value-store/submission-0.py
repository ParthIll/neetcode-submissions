class TimeMap:

    def __init__(self):
        # Map each key to a list of [timestamp, value] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        pairs = self.store[key]
        
        # Manual binary search to find the largest timestamp <= target
        left, right = 0, len(pairs) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]  # This is a potential candidate
                left = mid + 1       # Keep looking right for a closer/exact match
            else:
                right = mid - 1      # Too big, look left
                
        return res