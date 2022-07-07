# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1= ""
        str2= ""
        while l1 or l2:
            if l1:
                str1+= str(l1.val)
                l1 =l1.next
            if l2:
                str2+= str(l2.val)
                l2 =l2.next
        output = int(str1[::-1]) + int(str2[::-1])
        output =str(output)[::-1]
        i =1
        first = ListNode()
        first.val = output[0]
        tempo =first
        while i< len(output):
                current =ListNode()
                current.val=  int(output[i])
                tempo.next =current
                i+=1
                tempo =tempo.next
        return first    
        print(output)