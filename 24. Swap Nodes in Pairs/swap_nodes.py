# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        tempo =head
        while tempo and tempo.next is not None:
            cur = tempo.next.val
            cur1 =tempo.val
            tempo.next.val , tempo.val = tempo.val , tempo.next.val
            if i==0:
                new_head = tempo
            tempo =tempo.next.next
            i+=1
        if i==0:
            new_head = head
        return new_head