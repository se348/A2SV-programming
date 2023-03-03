# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-101)
        dummyNode.next = head
        
        prev = dummyNode
        curr = head
        
        while curr:
            
            if curr.next and curr.val == curr.next.val:    
                temp = curr.val
                while curr and curr.val == temp:
                    prev.next = curr.next
                    curr= prev.next
            else:
                prev= curr
                curr= curr.next
                
        
                    
        return dummyNode.next