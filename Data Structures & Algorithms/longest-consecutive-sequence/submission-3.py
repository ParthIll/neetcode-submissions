class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums ==[]:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        differences = [0]*(len(nums)-1)
        for i in range(len(nums)-1):
            differences[i] = nums[i+1]-nums[i]
        print(differences)
        differencesSet={}
        e = 0
        for difference in differences:
            if difference ==1:
                if e in differencesSet.keys():
                    differencesSet[e]=differencesSet[e]+1
                else:
                    differencesSet[e] = 1
            else:
                if difference !=0:
                    e+=1
                continue
        print(differencesSet)
        try:
            return max(differencesSet.values())+1
        except:
            return 1