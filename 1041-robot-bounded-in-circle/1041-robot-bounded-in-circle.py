class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        
        
        current_coordinate = [0, 0]
        
        current_directions = [0, 1]
        for i in range(4):
            for temp in instructions:
                if temp == "G":
                    current_coordinate[0] += current_directions[0]
                    current_coordinate[1] += current_directions[1]
                    continue

                current_directions[0], current_directions[1] = current_directions[1], current_directions[0]
                if temp == "L":
                    current_directions[0] *=  -1
                elif temp == "R":
                    current_directions[1] *= -1
            
            if current_directions == [0, 1] and current_coordinate == [0, 0]:
                return True
        return False
        
        
#         if current_coordinates == [0, 0] and current_directions == [0, 0]:
#             return True
        
#         for _ in range(5):
#             if current_coordinates == [0, 0] and current_directions == [0, 0]:
#                 return True
            
        
#         return False
        

        
        
        
        