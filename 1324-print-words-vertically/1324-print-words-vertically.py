class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        words = s.split()
        max_length =0
        
        for word in words:
            max_length = max(max_length, len(word))
        
        vertical_res = [[] for i in range(max_length)]
        
        for idx in range(max_length):
            for word_idx in range(len(words)):
                
                if idx >= len(words[word_idx]):
                    
                    vertical_res[idx].append(" ")
                    
                else:
                    vertical_res[idx].append(words[word_idx][idx])
        
        result =[]
        
        for word in vertical_res:
            new_word = "".join(word)
            result.append(new_word.rstrip())
            
        return result