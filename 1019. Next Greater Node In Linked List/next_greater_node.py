# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        tempo = head
        new_list = []
        monotonic_stack =[]
        position= -1
        while tempo:
            position+=1
            new_list.append(0)
            while monotonic_stack and monotonic_stack[-1][1]< tempo.val:
                index, val = monotonic_stack.pop()
                new_list[index] = tempo.val
            monotonic_stack.append((position, tempo.val))
            tempo =tempo.next
        return new_list