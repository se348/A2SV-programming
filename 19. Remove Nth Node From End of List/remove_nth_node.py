# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        llist =[]
        tempo =head
        while tempo:
            llist.append(tempo.val)
            tempo = tempo.next
        llist.pop(-n)
        if llist==[]:
            return None
        new_head= ListNode()
        new_head.val = llist[0]
        tempo = new_head
        for n in range(1, len(llist)):
            current = ListNode()
            current.val = llist[n]
            tempo.next = current
            tempo = tempo.next
        return new_head
            