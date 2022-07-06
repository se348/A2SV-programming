# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        custom_list =[]
        temp =head
        while temp != None:
            custom_list.append(temp.val)
            temp =temp.next
        if custom_list == custom_list[::-1]:
            return True
        return False