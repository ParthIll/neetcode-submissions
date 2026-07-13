class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        eff = [0]*len(gas)
        for i in range(len(eff)):
            eff[i]=gas[i]-cost[i]
        maxeff=max(eff)
        print(eff)
        if sum(eff)<0:
            return -1
        else:
            q=deque()
            for i in range(len(eff)):
                if eff[i]>=0:
                    if i+1 in range(len(eff)):
                        q.append((i,i+1,eff[i]+eff[i+1]))
                    else:
                        q.append((i,0,eff[i]+eff[0]))
            while q:
                x,y,z=q.popleft()
                if x==y:
                    return x
                if z<0:
                    continue
                if y+1==len(eff):
                    y=0
                else:
                    y+=1
                if z+eff[y]>=0:
                    q.appendleft((x,y,z+eff[y]))

            
