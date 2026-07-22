class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nCount = Counter(nums)
        k=nCount[val]
        l=len(nums)
        for i in range(k):
            nums.remove(val)


        return l-k