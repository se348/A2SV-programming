class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        ptr_left = 0
        ptr_right =0
        
        merge = []
        
        while ptr_left < len(word1) or ptr_right < len(word2):
            
            if ptr_right != len(word2) and (ptr_left == len(word1) or word2[ptr_right] > word1[ptr_left]):
                merge.append(word2[ptr_right])
                ptr_right += 1
            elif ptr_left != len(word1) and (ptr_right == len(word2) or word2[ptr_right] < word1[ptr_left]):
                merge.append(word1[ptr_left])
                ptr_left += 1
            elif word2[ptr_right] == word1[ptr_left]:
                temp_left = ptr_left + 1
                temp_right = ptr_right +1
                
                while temp_right != len(word2) and  temp_left!=len(word1) and word1[temp_left] == word2[temp_right]:
                    temp_right += 1
                    temp_left += 1
                
                    
                if  temp_right != len(word2) and (temp_left == len(word1) or word2[temp_right] > word1[temp_left]):
                    merge.append(word2[ptr_right])
                    ptr_right += 1
                else:
                    merge.append(word1[ptr_left])
                    ptr_left += 1
            
        
        return "".join(merge)