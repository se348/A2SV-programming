# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def dfs(self, curr):
        if not curr:
            return 0, 0
        idx, res = self.dfs(curr.next)
        if curr.val == 1:
            res += 2 ** (idx)
        return idx + 1, res
    
    def getDecimalValue(self, head: ListNode) -> int:
        return self.dfs(head)[1]