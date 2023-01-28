# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr_left = list1
        curr_right = list2
        curr_result = result
        
        while curr_left or curr_right:
            
            if curr_left is not None and (curr_right is None or curr_right.val > curr_left.val):
                curr_result.next = ListNode(curr_left.val)
                curr_left = curr_left.next
            
            else:
                curr_result.next = ListNode(curr_right.val)
                curr_right = curr_right.next
            
            curr_result = curr_result.next
                
        return result.next