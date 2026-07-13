class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fullSet = Counter(s)
        i=0
        start=0
        ret=[]
        while i<len(s):
            minset=Counter(s[start:i+1])
            startnew=True
            for key in minset:
                if minset[key]!=fullSet[key]:
                    startnew=False
            if startnew:
                ret.append(i+1-start)
                start=i+1
            i+=1
        return ret