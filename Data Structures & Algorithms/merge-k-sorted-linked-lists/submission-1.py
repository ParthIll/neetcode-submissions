import heapq
from typing import List, Optional

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tracer = dummy
        
        nodeHeap = []
        counter = 0  # Serves as a tie-breaker for identical node values
        
        # Initial push of the head of each list
        for node in lists:
            if node:
                # Tuple structure: (value, unique_id, node_object)
                heapq.heappush(nodeHeap, (node.val, counter, node))
                counter += 1
                
        while nodeHeap:
            # Unpack the three elements from the heap tuple
            val, _, node = heapq.heappop(nodeHeap)
            
            # Connect the popped node to our merged list
            tracer.next = node
            tracer = tracer.next
            
            # If the popped node has a next element, push it into the heap
            if node.next:
                heapq.heappush(nodeHeap, (node.next.val, counter, node.next))
                counter += 1
                
        return dummy.next
