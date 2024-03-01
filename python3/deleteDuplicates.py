# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        if a == None:
            return a
        if a.next == None:
            return a
        while a.next != None:
            if a.next.val == a.val:
                a.next = a.next.next
            else:
                a = a.next
        return head
