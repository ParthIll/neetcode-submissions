class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        visited=set()
        q=deque()
        q.append(0)
        while q:
            x=q.popleft()
            visited.add(x)
            if x==len(s)-1:
                return True
            for add in range(minJump,maxJump+1):
                if x+add in range(len(s)) and x+add not in visited and s[x+add]=="0":
                    q.appendleft(x+add)
        return False