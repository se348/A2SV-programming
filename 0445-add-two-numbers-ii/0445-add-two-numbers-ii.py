# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    def dfs(self, l1, l2):
        if not l1.next and not l2.next:
            temp = l1.val + l2.val
            l1.val = temp % 10
            return temp // 10
        
        temp = self.dfs(l1.next, l2.next) + l1.val + l2.val
        l1.val = temp % 10
        return temp // 10
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        length1, length2 = self.length(l1), self.length(l2)
        currL, currR = l1, l2
        
        if length1 < length2:
            for i in range(length2 - length1):
                currL = ListNode(0)
                currL.next = l1
                l1 = currL
        
        else:
            for i in range(length1 - length2):
                currR = ListNode(0)
                currR.next = l2
                l2 = currR
                
        val = self.dfs(l1, l2)
        
        if val != 0:
            temp = ListNode(val)
            temp.next = l1
            l1 = temp
        
        return l1