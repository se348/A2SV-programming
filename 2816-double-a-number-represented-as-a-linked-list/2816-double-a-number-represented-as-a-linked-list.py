# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def recursion(curr_node):
            if not curr_node:
                return 0
            
            nexxt = recursion(curr_node.next)
            curr_sum = nexxt + (curr_node.val * 2)
            curr_node.val = (curr_sum  % 10)
            
            return (curr_sum // 10)
        
        
        remainder = recursion(head)
        
        
        if remainder:
            nxt = ListNode(remainder)
            nxt.next = head
            return nxt        
        
        return head 