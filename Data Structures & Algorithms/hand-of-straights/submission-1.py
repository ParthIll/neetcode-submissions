class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        hand.sort()
        curGroup=[]
        while hand:
            if len(curGroup)==groupSize:
                curGroup=[]
            if curGroup==[]:
                curGroup.append(hand.pop())
                continue
            if curGroup[-1]-1 in hand:
                curGroup.append(hand.pop(hand.index(curGroup[-1]-1)))
            else:
                return False
            
            
        return True