# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slowPtr = head.next
        fastPtr = head.next.next
        
        while fastPtr and fastPtr.next and slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
        if not fastPtr or not fastPtr.next:
            return None
        while head != slowPtr:
            head = head.next
            slowPtr = slowPtr.next
            
        return slowPtr