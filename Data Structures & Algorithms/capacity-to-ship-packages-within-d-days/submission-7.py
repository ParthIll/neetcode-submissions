class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        # Helper function to check if capacity target is feasible
        def canShip(capacity: int) -> bool:
            needed_days = 1
            current_weight = 0
            
            for w in weights:
                if current_weight + w > capacity:
                    needed_days += 1
                    current_weight = w  # Start a new day
                else:
                    current_weight += w
            
            return needed_days <= days

        # Binary Search for the minimum valid capacity
        while low < high:
            mid = (low + high) // 2
            if canShip(mid):
                high = mid      # Try to find a smaller valid capacity
            else:
                low = mid + 1   # Capacity too small, increase it
                
        return low