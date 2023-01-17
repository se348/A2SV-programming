class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for start in range(len(names)):
            
            min_idx = start
            min_val = heights[start]
            
            for i in range(start, len(heights)):
                    
                if heights[i] > min_val:
                    
                    min_idx = i
                    min_val = heights[i]
                    
                
            heights[start], heights[min_idx] = heights[min_idx], heights[start]
            names[start], names[min_idx] = names[min_idx], names[start]
            
                
        return names
                    
                    
                    
                    