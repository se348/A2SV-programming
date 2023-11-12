# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        
        curr_count= 0
        curr_node = head
        connected_components = 0
        
        while curr_node:
            if curr_node.val in nums:
                curr_count += 1
            else:
                if curr_count != 0:
                    connected_components += 1
                curr_count = 0
            
            curr_node = curr_node.next
        if curr_count != 0:
            connected_components += 1
        return connected_components
        
        