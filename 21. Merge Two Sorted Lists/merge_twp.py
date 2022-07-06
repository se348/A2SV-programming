class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        soln = ListNode()
        ansList = soln
        computed = []
        while(list1):
            val1 = list1.val
            computed.append(val1)
            list1 = list1.next
        while(list2):
            val2 = list2.val
            computed.append(val2)
            list2 = list2.next
        computed.sort()
        for i in computed:
            ansList.next = ListNode(i)
            ansList = ansList.next
        return soln.next