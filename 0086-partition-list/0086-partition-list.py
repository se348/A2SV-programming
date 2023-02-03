# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    
        lessThan = ListNode(-1)
        greaterOrEqual = ListNode(-1)
        
        lessStart = lessThan
        greaterStart = greaterOrEqual
        curr = head
        
        while curr:
            val = curr.val
            
            if  val < x:
                lessThan.next = ListNode(val)
                lessThan = lessThan.next
            
            else:
                greaterOrEqual.next= ListNode(val)
                greaterOrEqual = greaterOrEqual.next
            
            curr = curr.next
        
        lessThan.next = greaterStart.next
        
        return lessStart.next