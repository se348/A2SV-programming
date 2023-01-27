class Solution:
    def maxArea(self, height: List[int]) -> int:
    
        maximumAr = 0 
        
        left = 0 
        right = len(height) - 1
        
        while left < right:
            
            maximumAr = max(maximumAr, min( height[right], height[left]) * (right -left))
            
            if height[left] > height[right]:
                right -= 1
            
            else:
                left += 1
                
        return maximumAr