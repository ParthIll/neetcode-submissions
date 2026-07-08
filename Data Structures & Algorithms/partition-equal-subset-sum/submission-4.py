class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tups=[(0,0)]
        tupset=set()
        for num in nums:
            i=0
            curlen=len(tups)
            while i <curlen:
                c1 = (tups[i][0],tups[i][1]+num)
                c2 = (tups[i][0]+num,tups[i][1])
                if c1 not in tupset:
                    tups.append(c1)
                    tupset.add(c1)
                if c2 not in tupset:
                    tups[i]=c2
                    tupset.add(c2)
                else:
                    tups.pop(i)
                    curlen-=1
                    i-=1
                i+=1
        print(tups)
        for tup in tups:
            if tup[0]==tup[1]:
                print("here:",tup)
                return True
        return False
                