# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        a = head
        b = head
        while b is not None and a is not None:
            if b.next is None:
                return False
            if b.next.next is None:
                return False
            a=a.next
            b=b.next.next
            if a == b:
                return True
        return False
