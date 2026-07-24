import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect.bisect_left(arr,x)
        arr.insert(ind,x)
        ret=[]
        l=ind-1
        r=ind+1
        for i in range(k):
            if l==-1:
                ret.append(arr[r])
                r+=1
                continue
            if r==len(arr):
                ret.append(arr[l])
                l-=1
                continue
            if(abs(arr[r]-x)<abs(arr[l]-x)):
                ret.append(arr[r])
                r+=1
            else:
                ret.append(arr[l])
                l-=1
        return sorted(ret)