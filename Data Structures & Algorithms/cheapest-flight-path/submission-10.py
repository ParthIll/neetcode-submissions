class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minPrice=10**9
        flightmap = defaultdict(list)
        for flight in flights:
            flightmap[flight[0]].append([flight[2],flight[1]])
        
        q=deque()
        for ticket in flightmap[src]:
            
            q.append(ticket+[k])
        
        print(flightmap)
        visited={}
        while q:

            price,x,kcount = q.popleft()
            
            if x==dst:
                minPrice = min(minPrice,price)
                continue
            if kcount<=0 or price>=minPrice:
                
                continue
            if (x, kcount) in visited and visited[(x, kcount)] <= price:
                continue
            visited[(x, kcount)] = price
            heap = flightmap[x].copy()
            while heap:
                y=heap.pop()
                q.append([y[0]+price,y[1],kcount-1])
            
            
        return minPrice if minPrice !=10**9 else -1