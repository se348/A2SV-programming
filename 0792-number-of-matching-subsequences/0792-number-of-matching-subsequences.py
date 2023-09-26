class TrieNode:
    def __init__(self):
        self.children = [ None ] * 26
        self.is_end = False
        self.valid_until = -1
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def findword(self,s, word) -> bool:
        current = self.root
        idx = -1
        for i in range(len(word)):
            diff = ord(word[i]) - ord('a')
            
            if current.children[diff].valid_until == -1:
                idx += 1
                while idx < len(s) and s[idx] != word[i]:
                    idx += 1
                if idx == len(s):
                    current.children[diff].valid_until = -10
                    return False
                else:
                    current.children[diff].valid_until = idx
            
            elif current.children[diff].valid_until == -10:
                return False
            else:
                idx = current.children[diff].valid_until
                
            current = current.children[diff]
        return True
        
    def insert_word(self, word):
        def insert_with_ptr(prev: TrieNode, ind: int):
            curr_letter = ord(word[ind])  
            
            to_be_added = prev.children[curr_letter -  ord('a')]
            
            if not to_be_added:
                curr_node = TrieNode()
                
                prev.children[curr_letter -  ord('a')] = curr_node
                to_be_added = curr_node
                
            if ind == len(word) - 1:
                to_be_added.is_end = True
            else:
                insert_with_ptr(to_be_added, ind + 1)
            
        insert_with_ptr(self.root, 0) 

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        count = 0
        
        for i in range(len(words)):
            word = words[i]
            trie.insert_word(word)
            
            if trie.findword(s, word):
                count += 1
            # print(trie.root.children[21].children[12].valid_until)
        return count
            