class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        turns = 0
        targ = [int(s)for s in target]
        deads=set(tuple([int(s) for s in strs]) for strs in deadends)
        cur=[0,0,0,0]
        if (0,0,0,0) in deads:
            return -1
        q=deque()
        q.append(cur)
        visited=set()
        while q:

            for i in range(len(q)):

                x=q.popleft()
                
                if x==targ:
                    return turns
                for i in range(4):
                    qsub = x.copy()
                    if qsub[i]>0:
                        qsub[i]-=1
                    else:
                        qsub[i]=9
                    qadd = x.copy()
                    if qadd[i]<9:
                        qadd[i]+=1
                    else:
                        qadd[i]=0
                    if tuple(qadd) not in deads and tuple(qadd) not in visited:  
                        visited.add(tuple(qadd))
                        q.append(qadd)
                    if tuple(qsub) not in deads and tuple(qsub) not in visited:
                        visited.add(tuple(qsub))
                        q.append(qsub)
            turns+=1
        return -1