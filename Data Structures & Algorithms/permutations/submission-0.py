class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        cur=[[nums[0]]]
        for num in nums[1:]:
            new_perms=[]
            for perm in cur:
                for i in range(len(perm)+1):
                    permcopy = perm.copy()
                    permcopy.insert(i,num)
                    new_perms.append(permcopy)
            cur=new_perms
        return cur                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     