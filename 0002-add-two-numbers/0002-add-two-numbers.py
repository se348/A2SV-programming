# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tail1 = l1
        tail2 = l2
        print(tail1)
        print(tail2)
        
        prev = None
        
        dummyNode = ListNode(-1)
        dummyNode.next = l1
        
        curr= dummyNode 
        remain = 0
        
        while tail1 or tail2:
            
            if not tail1:
                value  = (tail2.val + remain) % 10
                remain = (tail2.val + remain)// 10
                temp = ListNode(value)
                curr.next = temp
                tail2 = tail2.next
            
            elif not tail2:
                value  = (tail1.val + remain) % 10
                remain = (tail1.val + remain)// 10
                temp = ListNode(value)
                curr.next = temp
                tail1 = tail1.next
                
            else:
                value  = (tail2.val + tail1.val + remain) % 10
                remain = (tail2.val + tail1.val + remain)// 10
                temp = ListNode(value)
                curr.next =temp
                tail1 = tail1.next
                tail2 = tail2.next

            curr = curr.next
        if remain != 0:
            curr.next = ListNode(remain)
            
        return dummyNode.next