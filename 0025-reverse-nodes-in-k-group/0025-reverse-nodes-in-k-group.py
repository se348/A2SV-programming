# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findSize(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def reverse(self, prev, k):
        first = prev.next
        curr_prev= None
        
        curr = first
        for i in range(k):
            tempo = curr.next
            curr.next = curr_prev
            curr_prev = curr
            curr = tempo
        first.next = curr
        prev.next = curr_prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        count = self.findSize(head)
        curr = 0
        
        node = dummyNode
        
        while curr + k <= count:
            self.reverse(node, k)
            
            for i in range(k):
                node = node.next
            curr += k
            
        return dummyNode.next