class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(lambda: None)
  
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.children = defaultdict(lambda: None)
        
    def insert(self, word: str) -> None:
        def insertWithPtr(prev: TrieNode, ind: int):
            curr_letter = word[ind]
            
            to_be_added = prev.children[curr_letter]
            
            if not to_be_added:
                curr_node = TrieNode()
                
                prev.children[curr_letter] = curr_node
                to_be_added = curr_node
                
            if ind == len(word) - 1:
                to_be_added.is_end = True
            else:
                insertWithPtr(to_be_added, ind + 1)
            
        insertWithPtr(self.root, 0)            
    
  
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        trie = Trie()
        
        try:
            for word in strs:
                trie.insert(word)
        except:
            return ""
        
        current = trie.root
        res = []
        
        while len(current.children) == 1:
            
            the_key = list(current.children.keys())[0]
            res.append(the_key)
            current = current.children[the_key]
            if current.is_end:
                break
        
        
        return "".join(res)
        