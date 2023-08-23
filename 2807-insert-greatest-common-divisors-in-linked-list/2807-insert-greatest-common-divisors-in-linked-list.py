# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, num1, num2):
        if num2 == 0:
            return num1
        return gcd(num2, num1 % num2)
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr.next:
            nxt = curr.next
            val  = self.gcd(curr.val, nxt.val)
            node = ListNode(val)
            node.next = nxt
            curr.next = node
            curr =nxt
            
        return head