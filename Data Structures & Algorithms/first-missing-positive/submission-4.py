class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nset=set(nums)
        minNot=max(1,max(nums)+1)
        for i in range(1,minNot):
            if i not in nset:
                minNot=i
                break

        return minNot
