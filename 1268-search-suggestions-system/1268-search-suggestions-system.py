class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False
        self.words = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        
        current = self.root
        
        for i in range(len(word)):
            diff = ord(word[i]) - ord("a") 
            
            if not current.children[diff]:
                current.children[diff] = TrieNode()
            
            if len(current.children[diff].words) != 3:
                current.children[diff].words.append(word)
                
            current= current.children[diff]
            
        current.is_word = True
        
    def search(self, word):
                
        current = self.root
        res = []
        
        for i in range(len(word)):
            diff = ord(word[i]) - ord('a')      
            nxt = current.children[diff]
            
            if not nxt:
                res.extend([[] for j in range(len(word) - i)])
                return res
            
            res.append(nxt.words)            
            current = nxt
        
        return res
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        
        for word in products:
            trie.insert(word)
        
        return trie.search(searchWord)
        