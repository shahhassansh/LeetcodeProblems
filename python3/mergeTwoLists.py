# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        out = head
        p1, p2 = l1, l2
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                out.next = p1
                p1 = p1.next
            else:
                out.next = p2
                p2 = p2.next
            out = out.next
        if p1 != None:
            out.next = p1
        if p2 != None:
            out.next = p2
        return head.next
