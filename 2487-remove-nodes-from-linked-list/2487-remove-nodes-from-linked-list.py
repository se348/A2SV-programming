# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,prev, head):
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self.reverse(head, temp)
    
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(None, head)
        
        result = None
        
        curr = head
        prev = 0
        
        while curr:
            if curr.val >= prev:
                temp = ListNode(curr.val)
                temp.next = result
                result = temp
                prev = curr.val
            curr = curr.next
        return result
                
        
    