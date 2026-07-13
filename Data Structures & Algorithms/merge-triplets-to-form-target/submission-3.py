class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good=set()
        for trip in triplets:
            gAdd=[]
            for i in range(len(trip)):
                if trip[i]>target[i]:
                    gAdd.clear()
                    break
                if trip[i]==target[i]:
                    gAdd.append(i)
            for g in gAdd:
                good.add(g)
        for i in range(len(target)):
            if i not in good:
                return False
        return True