# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None:
            return 0
        slow = head
        fast = head.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head
        while curr != None:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp
        
        rev = prev
        s = 0
        maxs = 0
        while rev!= None:
            s =  rev.val +head2.val
            maxs = max(s, maxs)
            rev = rev.next
            head2 = head2.next
        return maxs


        
        
