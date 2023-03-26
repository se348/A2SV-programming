class MyHashSet:

    def __init__(self):
        self.head = ListNode(-1)

    def add(self, key: int) -> None:
        curr = self.head
        prev = None
        
        while curr:
            if curr.val == key:
                return 
            prev = curr
            curr =curr.next
            
        prev.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        curr = self.head
        prev = None
        
        while curr:
            if curr.val == key:
                prev.next =curr.next
                return
            else:
                prev = curr
                curr =curr.next
                
    def contains(self, key: int) -> bool:
        curr = self.head
        
        while curr:
            if curr.val == key:
                return True
            curr =curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)