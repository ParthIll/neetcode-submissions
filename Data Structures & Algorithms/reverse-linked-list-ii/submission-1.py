# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        beg=ListNode()
        beg.next=head
        if left==right:
            return beg.next
        lbef=beg
        for i in range(1,left):
            lbef=head
            head=head.next
        l=head
        for i in range(right-left):
            head=head.next
        rright=head.next
        lsave=l
        prev=l
        l=l.next
        while l!=rright:
            
            nex=l.next
            l.next=prev
            prev=l
            l=nex
        lbef.next=prev
        lsave.next=rright
        return beg.next