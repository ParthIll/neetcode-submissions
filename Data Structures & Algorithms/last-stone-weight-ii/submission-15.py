class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        visited=set()
        stones.sort()
        
        q=deque()
        q.append(stones)
        minp=9999999
        while q:
            arr=q.popleft()
            if tuple(arr) in visited:
                continue
            visited.add(tuple(arr))
            if len(arr)==1:
                minp=min(arr[0],minp)
                continue
            elif len(arr)==0:
                return 0
            for i in range(0,min(len(arr)-1,2)):
                j=i+1
                if arr[j]>arr[i]:
                    i,j=j,i
                    new=arr.copy()
                    new[i]=arr[i]-arr[j]
                    new=new[:j]+new[j+1:]                        
                    if tuple(new) not in visited:
                        q.append(new)
                elif arr[i]>arr[j]:
                    
                    new=arr.copy()
                    new[i]=arr[i]-arr[j]
                    new=new[:j]+new[j+1:]                        
                    if tuple(new) not in visited:
                        q.append(new)
                else:
                    new=arr.copy()
                    new=new[:j]+new[j+1:]
                    new = new[:i]+new[i+1:]
                    if tuple(new) not in visited:
                        q.append(new)
            i=0
            j=len(arr)-1
            if arr[j]>arr[i]:
                    i,j=j,i
                    new=arr.copy()
                    new[i]=arr[i]-arr[j]
                    new=new[:j]+new[j+1:]                        
                    if tuple(new) not in visited:
                        q.append(new)
            elif arr[i]>arr[j]:
                
                new=arr.copy()
                new[i]=arr[i]-arr[j]
                new=new[:j]+new[j+1:]                        
                if tuple(new) not in visited:
                    q.append(new)
            else:
                new=arr.copy()
                new=new[:j]+new[j+1:]
                new = new[:i]+new[i+1:]
                if tuple(new) not in visited:
                    q.append(new)
                       
            

        
        return minp