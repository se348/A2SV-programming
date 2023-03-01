# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        
        dummyNode.next = head
        
        curr = dummyNode.next
        prev = dummyNode
        
        while curr and curr.next:
            temp = curr.next.next
            prev.next = curr.next
            prev= prev.next
            prev.next= curr
            curr.next = temp
            curr = temp
            prev= prev.next
            
        return dummyNode.next
        