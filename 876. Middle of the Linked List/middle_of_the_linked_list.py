# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]):
        tempo= head
        counter=0
        while tempo!= None:
                counter +=1
                tempo =tempo.next
        middle =counter//2
        counter2 =0
        tempo =head
        while counter2 != middle:
                tempo =tempo.next
                counter2+=1
        return tempo