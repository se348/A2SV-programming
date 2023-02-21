# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insert(self, dummyNode, value):
        curr = dummyNode
        
        while curr and curr.val < value.val:
            if curr.next and curr.next.val < value.val:
                curr = curr.next
                
            elif curr.next and curr.next.val >= value.val:
                temp =curr.next
                value.next = temp
                curr.next = value 
                return value
        
        
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(-5001)
        dummyNode.next = head
        
        prev= dummyNode
        curr= head
        
        while curr:
            
            if curr.val < prev.val:
                prev.next = prev.next.next
                prev =self.insert(dummyNode, curr)
                curr = prev.next
            
            else:
                prev= curr
                curr = curr.next
                
        return dummyNode.next
                