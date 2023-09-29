class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.score = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.smallcase_a = 97
        
    def insert(self, word: str, score) -> None:
        def insertWithPtr(prev: TrieNode, ind: int, score):
            curr_letter = ord(word[ind])  
            
            to_be_added = prev.children[curr_letter -  self.smallcase_a]
            
            if not to_be_added:
                curr_node = TrieNode()
                
                prev.children[curr_letter -  self.smallcase_a] = curr_node
                to_be_added = curr_node
            
            to_be_added.score += score
                
            if ind != len(word) - 1:
                insertWithPtr(to_be_added, ind + 1, score)
            
        insertWithPtr(self.root, 0, score)            
    
    def search(self, word: str) -> bool:
        
        current = self.root
        min_res = 0
        for i in range(len(word)):
            if not current.children[ord(word[i]) - self.smallcase_a]:
                return 0
            min_res = current.children[ord(word[i]) - self.smallcase_a].score
            current = current.children[ord(word[i]) - self.smallcase_a]
        return min_res
        
class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.diction ={}
        
    def insert(self, key: str, val: int) -> None:
        prev_val = val
        if key in self.diction:
            val -= self.diction[key]
            
        self.diction[key] = prev_val
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)

