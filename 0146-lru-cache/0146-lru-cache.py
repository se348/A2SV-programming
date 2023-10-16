class ListNode:
    def __init__(self, key, value = None,prev=None, nxt=None):
        self.key = key
        self.val = value
        self.nxt = nxt
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.headNode = ListNode(-1)
        self.tailNode = ListNode(-1)
        self.count = 0
        self.capacity = capacity
        self.dictionary = {}
        
        self.headNode.nxt = self.tailNode
        self.tailNode.prev = self.headNode
        
    def get(self, key: int) -> int:
        if key not in self.dictionary:
            return -1
        
        node = self.dictionary[key]
        next_node = node.nxt
        prev_node = node.prev
        prev_node.nxt = next_node
        next_node.prev = prev_node
        
        tail_prev = self.tailNode.prev
        tail_prev.nxt = node
        node.prev = tail_prev
        
        self.tailNode.prev = node
        node.nxt =  self.tailNode
        
        return node.val
        
        
            
    def put(self, key: int, value: int) -> None:
            
        if not (key in self.dictionary):
            if self.count < self.capacity:

                node = ListNode(key, value)
                prev_node = self.tailNode.prev

                prev_node.nxt = node
                node.prev = prev_node

                node.nxt =self.tailNode
                self.tailNode.prev = node

                self.dictionary[key] = node
                self.count += 1
            else:
                to_be_removed = self.headNode.nxt
                key_remove = to_be_removed.key 
                self.dictionary.pop(key_remove)
                
                next_node = to_be_removed.nxt
                next_node.prev = self.headNode
                self.headNode.nxt = next_node
                
                node = ListNode(key, value)
                prev_node = self.tailNode.prev

                prev_node.nxt = node
                node.prev = prev_node

                node.nxt =self.tailNode
                self.tailNode.prev = node

                self.dictionary[key] = node

        else:
            self.get(key)
            self.tailNode.prev.val = value
            
            
        
       
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)