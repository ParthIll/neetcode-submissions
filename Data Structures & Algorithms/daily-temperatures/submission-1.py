from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack=deque()
        for i in range(len(temperatures)):
            if not stack:
                stack.append([temperatures[i],i])
                continue
            if temperatures[i]<=stack[-1][0]:
                stack.append([temperatures[i],i])
            else:
                j=1
                while stack[-1][0]<temperatures[i]:
                    res[stack[-1][1]]=i-stack[-1][1]
                    stack.pop()
                    if not stack:
                        break
                stack.append([temperatures[i],i])
        return res