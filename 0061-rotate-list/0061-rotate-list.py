# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countLength(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        return count
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        count = self.countLength(head)
        
        k = count - (k % count)
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        curr= head
        prev = None
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        dummyNode.next = prev
        
        new_curr = curr
        new_prev = None
        while new_curr:
            temp = new_curr.next
            new_curr.next = new_prev
            new_prev = new_curr
            new_curr = temp
        
        head.next = new_prev
        
        curr = prev
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        dummyNode.next = prev
        
        return dummyNode.next
        