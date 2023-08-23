# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        number = 0
        
        while curr:
            number *= 10
            number += curr.val
            curr =curr.next
            
        number *= 2
        
        multiples = 1
        curr_num = number
        
        while curr_num >= 10:
            curr_num //= 10
            multiples *= 10
        
        curr = head
        tail = None
        
        while curr:
            n = (number // multiples)
            curr.val = n            
            number %= multiples
            multiples //= 10
            tail = curr
            curr = curr.next
        
        if multiples:
            tail.next = ListNode(number)
        
        return head