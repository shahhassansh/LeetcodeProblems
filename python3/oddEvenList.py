# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        odd = head 
        even = head.next
        even_head = even
        itr = even.next
        while itr != None and itr.next!= None:
            odd.next = itr
            odd = odd.next
            even.next = itr.next
            even = even.next
            itr = itr.next.next
        even.next = None
        if itr != None:
            odd.next = itr
            odd = odd.next
        odd.next = even_head
        return head
        
