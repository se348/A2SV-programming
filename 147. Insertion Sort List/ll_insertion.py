# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        llist =[]
        tempo =head
        while tempo:
            llist.append(tempo.val)
            tempo = tempo.next
        llist.sort()
        new_head= ListNode()
        new_head.val = llist[0]
        tempo = new_head
        for n in range(1, len(llist)):
            current = ListNode()
            current.val = llist[n]
            tempo.next = current
            tempo = tempo.next
        return new_head
    