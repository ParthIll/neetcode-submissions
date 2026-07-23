class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=0
        ret=[]
        r=0
        while l<len(nums1) and r<len(nums2):
            if l>=m-n and nums1[l]==0:
                nums1[l]=nums2[r]
                l+=1
                r+=1
                continue
            if nums1[l]>=nums2[r]:
                nums1.insert(l,nums2[r])
                nums1.pop()
                l+=1
                r+=1
                continue
            elif nums1[l]<nums2[r]:
                l+=1
        
            
        