class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        q=deque()
        q.append((0,0,0))
        if s1+s2==s3 or s2+s1==s3:
            return True
        memo=set()
        while q:
            x,y,z = q.popleft()
            if (x,y,z) in memo:
                continue
            memo.add((x,y,z))
            if z==len(s3) and x==len(s1) and y==len(s2):
                return True
            if z==len(s3):
                continue
                
            if x not in range(len(s1)) and y not in range(len(s2)):
                continue
            if x in range(len(s1)) and y in range(len(s2)) and s1[x]==s3[z] and s2[y]==s3[z]:
                q.append((x+1,y,z+1))
                q.append((x,y+1,z+1))
                continue
            if x in range(len(s1)) and s1[x]==s3[z]:
                q.append((x+1,y,z+1))
            elif y in range(len(s2)) and s2[y]==s3[z]:
                q.append((x,y+1,z+1))
            
            
        return False
            