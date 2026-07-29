class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cur=[[nums[0]]]
        for num in nums[1:]:
            new_perms=[]
            for perm in cur:
                for i in range(len(perm)+1):
                    permcopy = perm.copy()
                    permcopy.insert(i,num)
                    new_perms.append(permcopy)
            cur=new_perms
        vis=set()
        i=0
        l=len(cur)
        while i<l:
            if tuple(cur[i]) in vis:
                cur.pop(i)
                i-=1
                l-=1
            vis.add(tuple(cur[i]))
            i+=1
        return cur  