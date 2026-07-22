class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nCount=Counter(nums)
        nums[:nCount[0]]=[0]*nCount[0]
        nums[nCount[0]:nCount[0]+nCount[1]]=[1]*nCount[1]
        nums[nCount[0]+nCount[1]:]=[2]*nCount[2]
        return