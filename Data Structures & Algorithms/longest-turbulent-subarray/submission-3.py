class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        diffs=[0]*(len(arr)-1)
        if len(arr)==1:
            return 1
        for i in range(len(arr)-1):
            diffs[i]=arr[i+1]-arr[i]
        maxlongest=1
        longest=1
        neg=diffs[0]<0
        pos=diffs[0]>0
        eq=diffs[0]==0
        print(diffs)
        if not eq:
            longest+=1
            maxlongest+=1
        i=1
        while i<len(diffs):
            
            
            newneg=diffs[i]<0
            newpos=diffs[i]>0
            neweq=diffs[i]==0
            if pos:
                if newneg:
                    longest+=1
                else:
                    longest=2
            elif neg:
                if newpos:
                    longest+=1
                else:
                    longest=2
            else:
                if not neweq:
                    longest=2
                else:
                    longest=1
           
            pos,neg,eq=newpos,newneg,neweq
            
            print(i,longest,maxlongest)
            maxlongest=max(longest,maxlongest)
            i+=1
        return maxlongest