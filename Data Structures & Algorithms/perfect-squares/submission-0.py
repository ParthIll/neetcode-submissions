class Solution:
    def numSquares(self, n: int) -> int:
        nums=[]
        for i in range(1,n+1):
            if i*i>n:
                break
            else:
                nums.append(i*i)
        
        reached=defaultdict(int)
        reached[n]=0
        turns=1
        while 0 not in reached or not reached[0]:
            keys = list(reached.keys())
            for k in keys:
                for n in nums:
                    if reached[k-n]!=0:
                        continue
                    else:
                        reached[k-n] =turns
                    if k-n==0:
                        return reached[0]
            turns+=1

        return -1
