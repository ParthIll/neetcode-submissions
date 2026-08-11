class Solution:
    def integerBreak(self, n: int) -> int:
        res=[]
        maxsum=1
        choices =[3,2,1]
        q=deque()
        for i in range(len(choices)):
            q.append((choices[i],[i]))
        while q:
            add,path = q.popleft()
            if add==n:
                if len(path)<2:
                    continue
                inret=[]
                possum=1
                for p in path:
                    inret.append(choices[p])
                    possum*=choices[p]
                maxsum=max(maxsum,possum)
                res.append(inret)
                continue
            for x in range(path[-1],len(choices)):
                if add+choices[x]<=n:
                    q.append((add+choices[x],path+[x]))
        return maxsum        

