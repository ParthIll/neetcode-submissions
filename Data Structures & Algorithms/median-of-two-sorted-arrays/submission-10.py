class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_half = (m + n + 1) // 2  # Total elements on the left side
        
        while left <= right:
            # Partition index for nums1
            partition1 = (left + right) // 2
            # Partition index for nums2 guarantees exact total_half count
            partition2 = total_half - partition1
            
            # Identify the boundary elements around our partitions
            # Using float('-inf') / float('inf') handles out-of-bounds cases elegantly
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # If total combined length is odd
                if (m + n) % 2 != 0:
                    return float(max(maxLeft1, maxLeft2))
                # If total combined length is even
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                
            elif maxLeft1 > minRight2:
                # nums1's left side is too large; we must shift partition1 to the left
                right = partition1 - 1
            else:
                # nums1's left side is too small; we must shift partition1 to the right
                left = partition1 + 1
                
        return 0.0