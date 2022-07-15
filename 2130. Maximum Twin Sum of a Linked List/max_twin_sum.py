# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stck =[]
        answer= 0
        tempo = head
        while tempo:
            stck.append(tempo.val)
            tempo =tempo.next
        tempo= head
        i=0
        while i <= len(stck):
            curr2 = stck.pop()
            curr1 = tempo.val
            answer = max(answer, curr1+ curr2)
            tempo = tempo.next
            i+=1
        return answer