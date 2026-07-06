import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build map and sort destinations in reverse order upfront
        # Reverse sorting allows us to pop() efficiently from the end of the list (O(1))
        netMap = collections.defaultdict(list)
        for fro, to in tickets:
            netMap[fro].append(to)
            
        for fro in netMap:
            netMap[fro].sort(reverse=True)
            
        ret = []
        
        def dfs(airport):
            # While this airport has valid outgoing flights...
            while netMap[airport]:
                next_dest = netMap[airport].pop()
                dfs(next_dest)
            # If an airport has no more outgoing flights, it means we've hit 
            # either the final destination or the end of a sub-loop.
            ret.append(airport)
            
        dfs("JFK")
        
        # Since we append on the way back up, the itinerary is backwards. 
        # We reverse it to get the correct chronological order.
        return ret[::-1]