class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tCount = Counter(tasks)
        time=0
        cool=n+1
        while tCount:
            dels=[]
            for k in tCount:
                cool-=1
                
                time+=1
                tCount[k]-=1
                if tCount[k]==0:
                    dels.append(k)
                if cool==0:
                    break
                
            for de in dels:
                del tCount[de]
            if tCount:
                time+=cool
                cool=n+1
            tCount= dict(sorted(tCount.items(), key=lambda item: item[1],reverse=True))
        return time
