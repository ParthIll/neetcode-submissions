class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        stones=[()]*len(stoneValue)
        try:
            stones[-1]=(stoneValue[-1],-2**31,-2**31)
        except:
            print("fail")
        try:
            stones[-2] = (stoneValue[-2]-max(stones[-1]),stoneValue[-1]+stoneValue[-2],-2**31)
        except:
            print("fail")
        try:
            stones[-3] = (stoneValue[-3]-max(stones[-2]),(stoneValue[-3]+stoneValue[-2])-max(stones[-1]),stoneValue[-3]+stoneValue[-2]+stoneValue[-1])
        except:
            print("fail")
        for i in range(len(stones)-4,-1,-1):
            stones[i]=(stoneValue[i]-max(stones[i+1]),(stoneValue[i]+stoneValue[i+1])-max(stones[i+2]),stoneValue[i]+stoneValue[i+1]+stoneValue[i+2]-max(stones[i+3]))
        
        a=0
        b=0
        turn=True
        i=0
        while i<len(stones):
            choices =list(stones[i])
            if turn:
                a+=sum(stoneValue[i:i+1+choices.index(max(choices))]) 
            else:
                b+= sum(stoneValue[i:i+1+choices.index(max(choices))]) 
            i+=1+list(choices).index(max(choices)) 
            turn=not turn
        if b>a:
            return "Bob"
        if a>b:
            return "Alice"
        return "Tie"