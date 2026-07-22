from collections import deque
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort so we only build combinations in non-decreasing index order
        nums.sort()
        
        # Store state as: (remaining_target, start_index, path)
        q = deque([(target, 0, [])])
        res = []

        while q:
            rem, start_idx, path = q.popleft()

            if rem == 0:
                res.append(path)
                continue

            # Only pick numbers at or after start_idx
            for i in range(start_idx, len(nums)):
                num = nums[i]
                if rem - num >= 0:
                    q.append((rem - num, i, path + [num]))
                else:
                    # Early exit: since nums is sorted, further elements will also be too big
                    break

        return res