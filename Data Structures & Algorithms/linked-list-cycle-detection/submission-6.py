# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        valmap={}
        i=0
        while head and i<10:
            print(head.val)
            print(valmap)
            valmap[head]=valmap.get(head,0)+1
            if head.next in valmap:
                return True
            print(head.val)
            head=head.next
            i+=1
            
        return False