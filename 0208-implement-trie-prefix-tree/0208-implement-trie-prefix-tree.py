class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        
    
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.smallcase_a =97
        
    def insert(self, word: str) -> None:
        def insertWithPtr(prev: TrieNode, ind: int):
            curr_letter = ord(word[ind])  
            
            to_be_added = prev.children[curr_letter -  self.smallcase_a]
            
            if not to_be_added:
                curr_node = TrieNode()
                
                prev.children[curr_letter -  self.smallcase_a] = curr_node
                to_be_added = curr_node
                
            if ind == len(word) - 1:
                to_be_added.is_end = True
            else:
                insertWithPtr(to_be_added, ind + 1)
            
        insertWithPtr(self.root, 0)            
    
    def search(self, word: str) -> bool:
        current = self.root
        
        for i in range(len(word)):
            curr_ind  = ord(word[i]) - self.smallcase_a
            if not current.children[curr_ind]:
                return False
            current = current.children[curr_ind]
        
        return True if current.is_end else False
    
    def startsWith(self, word: str) -> bool:
        current = self.root
        
        for i in range(len(word)):
            curr_ind  = ord(word[i]) - self.smallcase_a
            if not current.children[curr_ind]:
                return False
            current = current.children[curr_ind]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)