from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists)> 1:
            for i in range(len(lists)//2):
                tempo = self.merge_lists_2(lists[i], lists[-1])
                lists.pop()
                lists[i] =tempo
        s= lists[0]
        while s:
            print(s.val)
            s= s.next
        return lists[0]
    
    def merge_lists_2(self,list1, list2):
        start =ListNode()
        tempo =start
        if list1 is None:
            return list2
        if list2 is None: return list1
        while list1 or list2:
            another_tempo =ListNode()
            if list1 and list2:
                if list1.val <=list2.val:
                    another_tempo.val =list1.val
                    list1 = list1.next
                else:
                    another_tempo.val =list2.val
                    list2 =list2.next
            elif list1:
                another_tempo.val =list1.val
                list1 =list1.next
            else:
                another_tempo.val =list2.val
                list2 =list2.next
            tempo.next =another_tempo
            tempo =tempo.next
            del another_tempo
        return start.next                
s= Solution()
head =ListNode(-1)
head2 =ListNode(5)
head3= ListNode(11)
head.next =head2
head2.next =head3

tail =ListNode(1)
tail2 =ListNode(3)
tail3= ListNode(4)
tail.next =tail2
tail2.next =tail3

hunger =ListNode(6)
hunger2 =ListNode(10)
hunger.next =hunger2

a= s.mergeKLists([None, head, None, hunger])