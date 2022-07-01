# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mine_list =[]
        tempo= head
        if head== None or head.next==None:
                return head
        while tempo:
                mine_list.append(tempo.val)
                tempo =tempo.next
        mine_list =mine_list[::-1]
        i =1
        first = ListNode()
        first.val = mine_list[0]
        tempo =first
        while i< len(mine_list):
                current =ListNode()
                current.val= mine_list[i]
                tempo.next =current
                i+=1
                tempo =tempo.next
        return first