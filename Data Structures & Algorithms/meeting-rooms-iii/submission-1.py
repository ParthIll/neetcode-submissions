class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [[(0,0)] for _ in range(n)]
        meetings.sort(key = lambda x:x[0])
        while meetings:
            st,end = meetings.pop(0)
            minStart = 9999999
            minRoom = 0
            found=False
            for i in range(len(rooms)):
                room = rooms[i]
                if room[-1][1] < st:
                    room.append((st,end))
                    found=True
                    break
                elif room[-1][1]<minStart:
                    minRoom = i
                    minStart = room[-1][1]
            if not found:
                rooms[minRoom].append((rooms[minRoom][-1][1],rooms[minRoom][-1][1]+(end-st)))
        
        maxLen = 0
        maxInd = 0
        for i in range(len(rooms)):
            if len(rooms[i])>maxLen:
                maxLen = len(rooms[i])
                maxInd = i
            
        print(rooms)
        return maxInd
