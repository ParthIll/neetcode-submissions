class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nCount = Counter(nums)
        ret=[]
        for key in nCount:
            if nCount[key]>(len(nums)//3):
                ret.append(key)
        return ret