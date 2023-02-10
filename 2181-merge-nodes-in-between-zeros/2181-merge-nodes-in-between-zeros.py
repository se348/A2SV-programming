# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        
        currNode = dummyNode
        temp = ListNode(0)
        
        
        while head:
            if head.val == 0:
                currNode.next = ListNode(temp.val)
                currNode = currNode.next
                temp = ListNode(0)
            else:
                temp.val += head.val
            head = head.next
            
        return dummyNode.next.next