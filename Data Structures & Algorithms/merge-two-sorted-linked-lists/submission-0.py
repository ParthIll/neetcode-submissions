class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the anchor for our new list
        dummy = ListNode()
        tail = dummy
        
        # 2. Iterate while both lists have nodes remaining
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1  # Link the smaller node
                list1 = list1.next # Move list1 pointer forward
            else:
                tail.next = list2  # Link the smaller node
                list2 = list2.next # Move list2 pointer forward
                
            tail = tail.next # Move our tail pointer forward
            
        # 3. If one list runs out of nodes, append the remainder of the other list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # The actual merged list starts right after the dummy node
        return dummy.next