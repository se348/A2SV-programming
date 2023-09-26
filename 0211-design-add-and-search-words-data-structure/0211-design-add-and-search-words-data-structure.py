class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        current = self.root
        
        for i in range(len(word)):
            
            curr_letter = word[i]
            diff = ord(curr_letter) - ord('a')
            
            node = current.children[diff]
            if not current.children[diff]:
                node = TreeNode()
                current.children[diff] = node
            
            current = node
        
        current.is_end = True
        

    def search(self, word: str) -> bool:
        
        def searchGivenIndex(word_ind, current) -> bool:
            curr_letter = word[word_ind]
            
            if curr_letter != ".":
                
                diff = ord(curr_letter) - ord('a')
                if not current.children[diff]:
                    return False
                
                if word_ind == len(word) - 1:
                    return current.children[diff].is_end
                
                if searchGivenIndex(word_ind + 1, current.children[diff]):
                    return True
                
                return False
            
            else:
                for i in range(26):
                    if not current.children[i]:
                        continue
                    
                    if word_ind == len(word) - 1:
                        if current.children[i].is_end:
                            return True
                    elif searchGivenIndex(word_ind + 1, current.children[i]):
                        return True
                return False
                    
        current = self.root
        return searchGivenIndex(0, current)
            
      