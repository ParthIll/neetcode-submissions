class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [0]*len(nums)
        haszeros=False
        allzeros = False
        counter=0
        if 0 in nums:
            haszeros=True
        for i in range(len(nums)):
            if nums[i] ==0:
                counter+=1
        if counter ==len(nums):
            allzeros=True
        if haszeros == False: 
            totalProd = 1
            for i in range(len(nums)):
                totalProd*=nums[i]
            for i in range(len(nums)):
                ret[i] = int(totalProd/nums[i])
        else:
            if allzeros == False:
                totalprod=1
                for i in range(len(nums)):
                    if nums[i]!= 0:
                        totalprod*=nums[i]
                for i in range(len(nums)):
                    if nums[i]!=0:
                        ret[i] = 0
                    else:
                        if counter >=2:
                            ret[i] = 0
                        else:
                            ret[i] = totalprod
            else:
                return [0]*len(nums)

        return ret