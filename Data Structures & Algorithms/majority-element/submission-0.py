class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nCount=Counter(nums)
        maj=0
        for key in nCount:
            if nCount[key]>len(nums)//2:
                maj=key
        return maj