class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        bCount = Counter(people)
        boats=0
        for i in range(limit,0,-1):
            if i not in bCount or bCount[i]==0:
                continue
            
            for x in range((limit-i)):
                if limit-(i+x) in bCount and bCount[limit-(i+x)]!=0:
                    for j in range(min(bCount[i],bCount[limit-(i+x)])):
                        
                        if bCount[i]==0:
                            break
                        if i ==limit-(i+x):
                            if bCount[i]==1:
                                break
                        boats+=1
                        bCount[i]-=1
                        bCount[limit-(i+x)]-=1
            boats+=bCount[i]
            
            
            print(bCount)
            bCount[i]=0
        
        return boats
