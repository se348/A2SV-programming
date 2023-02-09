# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findSize(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
    def findSecondHalf(self, head):
        count = self.findSize(head)
        for i in range(count//2):
            head = head.next
        second = head.next
        head.next = None
        return head, second
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        second = self.findSecondHalf(head)[1]
        second = self.reverse(second)
        first = head
        while first and second:
            temp = second.next
            second.next = first.next
            first.next = second
            second= temp
            first = first.next.next
        
        return head
        