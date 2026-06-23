class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Base case: mapping None to None simplifies the pointer lookups later
        nodemap = {None: None}
        
        # Pass 1: Create a cloned copy of every node and store it in the map
        curr = head
        while curr:
            nodemap[curr] = Node(curr.val)
            curr = curr.next
            
        # Pass 2: Wire up the next and random pointers for the clones
        curr = head
        while curr:
            nodemap[curr].next = nodemap[curr.next]
            nodemap[curr].random = nodemap[curr.random]
            curr = curr.next
            
        # Return the clone of the head node
        return nodemap[head]