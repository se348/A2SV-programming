class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        limit = len(heights) - 1
        
        
        
        while limit >= 0:
            
            for i in range( limit ):
                
                    
                if heights[i] < heights[i + 1]:
                    
                    heights[i], heights[ i + 1] =  heights[ i + 1], heights[i]
                    names[i], names[ i + 1 ] = names[i + 1], names[i]
                    
            limit -= 1
                
        return names
                    
                    
                    
                    