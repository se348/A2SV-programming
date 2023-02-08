# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findSize(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size = self.findSize(head)
        lists = []
        temp_list = []
        for i in range(k):
            curr = ListNode(-1)
            lists.append(curr)
            temp_list.append(curr)
            
        divide =  size //k
        modulo = size % k
        
        curr = head
        for i in range(k):
            
            for j in range(divide):
                temp = temp_list[i]
                temp.next = ListNode(curr.val)
                temp = temp.next
                temp_list[i] = temp
                
                curr =curr.next
            if modulo != 0:
                temp = temp_list[i]
                temp.next = ListNode(curr.val)
                temp = temp.next
                temp_list[i] = temp
                
                curr =curr.next
                modulo -= 1
                
        for i in range(len(lists)):
            lists[i] = lists[i].next
        return lists
            
            
            