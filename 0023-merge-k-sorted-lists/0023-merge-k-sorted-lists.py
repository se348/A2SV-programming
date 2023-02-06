# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myHeap = []
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        for node in lists:
            if node:
                heapq.heappush(myHeap, (node.val, node))
        
        dummyNode = ListNode(-1)
        curr = dummyNode
        
        while myHeap:
            val , node = heapq.heappop(myHeap)
            curr.next =ListNode(val)
            curr = curr.next
            if node.next:
                heapq.heappush(myHeap,(node.next.val, node.next))
                
        return dummyNode.next