class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets=[]
        for i in range(len(position)):
            time  = (target-position[i])/speed[i]
            fleets.append([position[i],time])
        fleets.sort(key =lambda fleet:fleet[0])
        fleetcnt=1
        maxim=0
        print(fleets)
        for j in range(len(fleets)-2,-1,-1):
            print(fleetcnt,j,maxim)
            maxim = max(float(fleets[j+1][1]),float(maxim))
            if fleets[j][1]<maxim:
                continue
            if(fleets[j][1])>fleets[(j+1)][1]:
                fleetcnt+=1
            else:
                maxim = max(float(fleets[j+1][1]),float(maxim))

            
        return fleetcnt