class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ret= []
        maxim = [0,0]
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
                
            else:
                freq[nums[i]] =1
        
        sorted_by_values_desc = {}
        sorted_by_values_desc = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        



        return list(sorted_by_values_desc.keys())[0:k]