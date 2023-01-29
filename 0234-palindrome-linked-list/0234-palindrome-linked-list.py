# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,prev, head):
        if not head:
            return prev
        nxt = head.next
        head.next = prev
        return self.reverse(head, nxt)
    
    def findMiddle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.findMiddle(head)
        start = self.reverse(None, middle)
        
        def check(head, start):
            if not start:
                return True
            elif start.val == head.val:
                return check(head.next, start.next)
            else:
                return False
            
        return check(head, start)