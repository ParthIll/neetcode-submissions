class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            numSum = numbers[i]+numbers[j]
            if numSum<target:
                i+=1
            elif numSum>target:
                j-=1
            else:
                return [i+1,j+1]