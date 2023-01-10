class Solution:
    def didwin(self,positions):
        new_positions = set(positions)
        
        for i,j in positions:
            if ( i+1 , j ) in new_positions and (i+2, j) in new_positions:
                print(i,j)
                return True

            elif (i+1, j+1) in new_positions and (i+2, j+2) in new_positions:
                return True

            elif (i,j+1) in new_positions and (i, j+2) in new_positions:
                return True

            elif (i+1, j-1) in new_positions and (i+2, j-2) in new_positions:
                return True
        return False
    
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = 0 
        y_count = 0
        x_positions = []
        o_positions = []
        
        for i, line in enumerate(board):
            for j, letter in enumerate(line):
                
                if letter == "X":
                    x_count += 1
                    x_positions.append((i,j))
                    
                elif letter == "O":
                    y_count += 1
                    o_positions.append((i,j))
                    
        diff = x_count - y_count
        # print(self.didwin(o_positions))
        # print(o_positions)
        if diff != 0 and diff != 1:
            return False
        if self.didwin(x_positions) and self.didwin(o_positions):
            return False
        if self.didwin(o_positions) and diff ==1:
            return False
        if self.didwin(x_positions) and diff ==0:
            return False
        if diff == 0 or diff == 1:
            return True
        
        return False
