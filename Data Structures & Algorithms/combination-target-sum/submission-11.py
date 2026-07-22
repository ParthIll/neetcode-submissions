class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        q=deque()
        for num in nums:
            q.append(([num],num))
        res=[]
        visited=set()
        while q:
            
            x,summ=q.popleft()
            
            
            if summ==target:
                res.append(x.copy())
                continue
            for num in nums:
                if summ+num<target:
                    xcopy=x.copy()
                    xcopy.append(num)
                    if tuple(sorted(Counter(xcopy).items())) in visited:
                        continue
            
                    visited.add(tuple(sorted(Counter(xcopy).items())))
                    q.append((xcopy,summ+num))
                elif summ+num==target:
                    xcopy=x.copy()
                    xcopy.append(num)
                    if tuple(sorted(Counter(xcopy).items())) in visited:
                        continue
            
                    visited.add(tuple(sorted(Counter(xcopy).items())))
                    res.append(xcopy)
        return res
            
            