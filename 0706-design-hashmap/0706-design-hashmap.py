class TrieNode:
    def __init__(self):
        self.children = [None] * 10
        self.value = -1
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key, value):
        current = self.root
        
        key = str(key)
        for i in range(len(key)):
            
            if not current.children[int(key[i])]:
                current.children[int(key[i])] = TrieNode()
                
            current = current.children[int(key[i])]
        
        current.value = value
    
    def remove(self, key):
        current = self.root
        
        key = str(key)
        for i in range(len(key)):
            if not current:
                return 
            current = current.children[int(key[i])]
        if not current:
            return 
        current.value = -1
    
    def get(self, key):
        current = self.root
        
        key = str(key)
        for i in range(len(key)):
            
            if not current:
                return -1
            current = current.children[int(key[i])]
        if not current:
            return -1
        return current.value
    
class MyHashMap:

    def __init__(self):
        self.trie = Trie()        

    def put(self, key: int, value: int) -> None:
        self.trie.insert(key, value)

    def get(self, key: int) -> int:
        return self.trie.get(key)

    def remove(self, key: int) -> None:
        self.trie.remove(key)

