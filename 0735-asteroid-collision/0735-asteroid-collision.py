class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
        
            while stack and (asteroid < 0  and stack[-1] > 0):
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                    
                elif abs(asteroid) > stack[-1]:
                    d = stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)
            
        return stack            
        
           