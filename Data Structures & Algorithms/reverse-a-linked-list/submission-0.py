class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list check (linked lists check against None, not [])
        if head is None:
            return None

        prev = None # 1. Added to keep track of the node behind us
        while head.next is not None:
            nxt = head.next       # 2. Save the real next node before breaking it
            head.next = prev      # 3. Point backward instead of creating a cycle
            prev = head           # 4. Move our trailing pointer up
            head = nxt            # 5. Advance your head pointer using the saved node
            
        head.next = prev # 6. Handle the very last node link change
        return head