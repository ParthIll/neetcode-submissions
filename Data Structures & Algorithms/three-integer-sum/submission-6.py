class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        i=0
        j=len(numbers)-1
        while(i<j):
            numSum = numbers[i]+numbers[j]
            if numSum<target:
                i+=1
            elif numSum>target:
                j-=1
            else:
                return [target*-1,numbers[i],numbers[j]]
        return []
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = {}
        nums.sort()
        for i in range(len(nums)):
            if i==0:
                newNums = nums[1:]
            elif i==len(nums)-1:
                newNums = nums[0:i]
            else:
                newNums = nums[:i] + nums[i+1:]  
            while(self.twoSum(newNums,nums[i]*-1)!=[]):
                ret[tuple(sorted(self.twoSum(newNums,nums[i]*-1)))]=1
                Leest = self.twoSum(newNums,nums[i]*-1)
                newNums.remove(Leest[1])
                newNums.remove(Leest[2])
        return list(ret)
        