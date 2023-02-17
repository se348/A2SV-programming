# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive(self, head, count):
        if not head:
            return count
        
        temp = self.recursive(head.next, count) -1
        
        if temp == 0:
            head.next = head.next.next

        return temp
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        self.recursive(dummyNode, n+1)
        
        return dummyNode.next