class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dropAt=[0]*(1001)
        trips.sort(key=lambda x:x[1])

        
        left=capacity
        for i in range(len(trips)):
            
            passe,froms,to = trips[i]
            left+=sum(dropAt[:froms+1])
            dropAt[:froms+1]=[0]*(froms+1)
            left-=passe
            if left<0:
                return False
            
            dropAt[to]+=passe
        return True