# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                if temp.next.next:
                    temp.next = temp.next.next
                else: temp.next= None
            else:
                temp = temp.next
        return head