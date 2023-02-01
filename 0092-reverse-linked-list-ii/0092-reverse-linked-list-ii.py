# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseSubPart(self, curr, count):
#         prev = None
#         final = None
#         zero_start_count = 0
#         start = None
        
#         while zero_start_count < count:
#             if zero_start_count == 0:
#                 final = curr
                
#             if zero_start_count == count -1:
#                 start = curr
                
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
#             zero_start_count += 1
        pass    
        # return final, start, curr
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        firstTie= dummyNode
        
        for _ in range(left - 1):
            firstTie = firstTie.next
        
        curr = firstTie.next
        firstTieEnd = curr
        
        prev = None
        for _ in range(right -left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        firstTie.next = prev
        firstTieEnd.next = curr
        
        return dummyNode.next