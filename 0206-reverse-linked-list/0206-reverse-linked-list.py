# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def recursive(self, prev, head):
    #     if not head:
    #         return prev
    #     forward = head.next
    #     head.next = prev
    #     return self.recursive(head, forward)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
        
        
        # return self.recursive(None, head)
        