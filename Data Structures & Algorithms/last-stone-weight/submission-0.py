class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones)>1:
            print(stones)
            y=stones[0]
            x=stones[1]
            if x==y:
                stones.pop(0)
                stones.pop(0)
                continue
            else:
                stones[0]=y-x
                stones.pop(1)
                stones.sort(reverse=True)
                continue
        if stones:
            return stones[0]
        else:
            return 0