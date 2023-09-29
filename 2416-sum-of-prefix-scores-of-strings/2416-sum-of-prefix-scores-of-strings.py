
class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.count = 0
       
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
            
            to_be_added.count += 1
    
            if ind != len(word) - 1:
                insertWithPtr(to_be_added, ind + 1)
                
        insertWithPtr(self.root, 0)            
    
    def search(self, word: str) -> bool:
        current = self.root
        count = 0
        
        for i in range(len(word)):
            curr_ind  = ord(word[i]) - self.smallcase_a
            current = current.children[curr_ind]
            count += current.count
        
        return count
    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        res = []
        
        for word in words:
            res.append(trie.search(word))
        
        return res