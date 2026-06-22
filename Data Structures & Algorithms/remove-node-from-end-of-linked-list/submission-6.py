# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        i=0
        size=0
        while head:
            size+=1
            head=head.next
        head=dummy.next
        n=size-n
        print(n)
        while i!=n and head.next:
            prev=head
            head=head.next
            i+=1
        if not head.next:
            try:
                if prev:
                    prev.next=None
                    return dummy.next
            except:
                return head.next
        if n==0:
            return dummy.next.next
        prev.next=head.next
        return dummy.next