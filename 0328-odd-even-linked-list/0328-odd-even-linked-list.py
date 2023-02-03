# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        curr = head
        tieptr = None
        
        while True:
            tieptr = curr
            if not curr.next or not curr.next.next:
                break
            curr = curr.next.next

        checker = tieptr
        
        curr = head
        while curr != checker:
            temp = curr.next.val
            curr.next = curr.next.next
            
            added = ListNode(temp)
            added.next = tieptr.next
            tieptr.next = added
            curr = curr.next
            tieptr = tieptr.next
            
        return head