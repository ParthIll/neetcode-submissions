class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        pCount = Counter(people)
        boats=0
        boats+=pCount[limit]
        for i in range(pCount[limit]):
            people.remove(limit)
        del pCount[limit]
        
        people.sort()
        l=0
        r=len(people)-1
        while people:
            
            if l==r:
                boats+=1
                if l-1>=0 and people[l-1]+people[l]<=limit:
                    people.pop(l)
                    people.pop(l-1)
                else:
                    people.pop(l)
                if not people:
                    break
                l=0
                r=len(people)-1
                continue
            if people[l]+people[r]==limit:
                people.pop(r)
                people.pop(l)
                boats+=1 
                l=0
                r=len(people)-1
            elif people[l]+people[r]<limit:
                l+=1
            elif people[l]+people[r]>limit:
                r-=1
        return boats
