"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping_dictionary = defaultdict(lambda: None)
        

        
        dummy = ListNode(-1)
        curr_new = dummy
        
        curr_old = head
        
        while curr_old:
            
            new_node = ListNode(curr_old.val)
            curr_new.next = new_node
            curr_new = curr_new.next
            mapping_dictionary[curr_old] = new_node
            curr_old = curr_old.next

        llist = list(mapping_dictionary.keys())
        
        for i in range(len(llist)):
            
            key = llist[i]
            value = mapping_dictionary[key]
            rand1 =key.random
            rand_mapped = mapping_dictionary[rand1]
            
            value.random = rand_mapped
            
        return dummy.next