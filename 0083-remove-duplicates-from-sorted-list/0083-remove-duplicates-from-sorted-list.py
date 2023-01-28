# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-101)
        curr = head
        curr_result = dummy
        
        while curr:
            
            if curr.val != curr_result.val:
                curr_result.next = ListNode(curr.val)
                curr_result = curr_result.next
            
            curr = curr.next
        
        return dummy.next