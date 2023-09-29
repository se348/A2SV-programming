class TrieNode:
    def __init__ (self):
        self.children = [None ] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        
        for i in range(len(word)):
            diff = ord(word[i]) - ord('a')
            temp = current.children[diff]
            
            if not temp:
                temp = TrieNode()
                current.children[diff] = temp
            
            current = current.children[diff]
            
        current.is_end = True
        
        
    def currLargest(self, currNode):
        
        maxim_res = []
        
        for i, neighbor in enumerate(currNode.children):
            
            if neighbor and neighbor.is_end:
                
                temp = self.currLargest(neighbor)
                temp.append(chr(i + 97))
                
                if len(temp) > len(maxim_res):
                    maxim_res = temp[:]
                
        return maxim_res
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        res = trie.currLargest(trie.root)
        return "".join(reversed(res))
