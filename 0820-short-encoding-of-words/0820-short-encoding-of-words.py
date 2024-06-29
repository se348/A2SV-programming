class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    
    def is_not_included(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return True
            curr = curr.children[ch]
        return len(curr.children) == 0
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        
        for i in range(len(words)):
            words[i]= words[i][::-1]
            trie.insert(words[i])
                
        res = 0
        set_repr = set(words)
        
        for word in set_repr:
            if trie.is_not_included(word):
                res += (len(word) + 1) 
            
        return res