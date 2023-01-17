class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for start in range(1, len(names)):
            
            curr = start
            
            while curr > 0 and heights[curr - 1] < heights[curr]:
                
                heights[curr -1], heights[curr] = heights[curr], heights[curr - 1]
                names[curr -1], names[curr] = names[curr], names[curr - 1]
                curr -= 1
                
            
        return names
                    
                    
                    
                    