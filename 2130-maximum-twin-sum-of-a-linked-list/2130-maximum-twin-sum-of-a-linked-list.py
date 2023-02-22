# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        length =0
        
        while curr:
            length += 1
            temp = curr.next
            curr.next = prev
            prev = curr
            curr =temp
            
        return prev, length
    
    def copy(self, head):
        temp = ListNode(head.val)
        new_head = temp
        
        while head:
            curr = ListNode(head.val)
            temp.next = curr
            head = head.next
            temp = temp.next
            
        return new_head
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        tail, length = self.reverse(self.copy(head))
        max_sum= 0
        for i in range(length//2 + 1):
            max_sum = max(max_sum, tail.val + head.val)
            
            tail = tail.next
            head = head.next
        
        return max_sum