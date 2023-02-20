# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummyNode = ListNode()
        dummyNode.next = list1
        prev= dummyNode
        curr =list1
        a_prev = None
        b_next = None
        count =0
        
        while curr:
            if count == a:
                a_prev = prev
            
            if count == b:
                b_next =curr.next
                break
                
            prev = curr
            curr = curr.next
            count += 1
          
        a_prev.next = list2
        curr = list2
        
        while curr.next:
            curr = curr.next
            
        curr.next = b_next
        return dummyNode.next