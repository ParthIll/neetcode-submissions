# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOver=0
        l3=ListNode()
        head=l3
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2=ListNode(0)
            fullsum =carryOver+l1.val + l2.val
            if fullsum<10:
                
                l3.val = fullsum
                
                l2=l2.next
                l1=l1.next
                carryOver=0
            else:
                l3.val = fullsum%10
                carryOver = fullsum//10
                l2=l2.next
                l1=l1.next
            if l1 or l2:
                l3.next = ListNode()
                l3=l3.next
            print(carryOver)
        if carryOver>0:
            l3.next=  ListNode(carryOver)
        return head