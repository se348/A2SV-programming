# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def count(self, curr):
        if not curr:
            return 0
        return 1 + self.count(curr.next)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_size = self.count(headA)
        b_size = self.count(headB)
        
        larger = max(a_size, b_size)
        smaller = min(a_size, b_size)
        start_indx =  larger - smaller
        
        for _ in range(start_indx):
            if a_size >= b_size:
                headA = headA.next
            else:
                headB = headB.next
        
        for _ in range(smaller):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
            
            