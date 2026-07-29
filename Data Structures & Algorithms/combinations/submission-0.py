class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output=[[]]
        for i in range(k):
            combs = []
            for j in range(1,n+1):
                
                for out in output:
                    if j not in out and (not out or j>out[-1]):
                        combs.append(out+[j])
            output=combs
        return output