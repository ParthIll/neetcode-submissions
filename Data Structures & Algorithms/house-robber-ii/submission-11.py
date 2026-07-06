class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        numms=list(nums)
        numms.append(0)
        numms.append(0)
        numms.append(0)
        save=numms[-4]
        def search(startZero):
            if startZero==True:
                numms[-4]=0
            else:
                numms[-4]=save
            for i in range(len(numms)-4,-1,-1):
                numms[i]=numms[i]+max(numms[i+2],numms[i+3])
        search(True)
        fir = numms[0]
        numms=list(nums)
        numms.append(0)
        numms.append(0)
        numms.append(0)
        
        search(False)
        sec= numms[1]
        thir=numms[2]
        print(fir,sec,numms)
        return max(fir,sec,thir)