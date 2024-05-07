class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        inbound= lambda x, y: 0 <= x< len(mat) and 0 <= y < len(mat[0])
        
        rows = len(mat)
        cols = len(mat[0])
        bit = 0
        
        for i in range(rows):
            for j in range(cols):
                
                if mat[i][j]:
                    curr_number = (i * cols) + (j + 1)
                    bit |= 1 << curr_number
        
        queue = deque([(bit, 0)])
        visited = set([bit])
        
        while queue:
            curr_bit, curr_step = queue.popleft()
            if not curr_bit:
                return curr_step
            
            for i in range(rows):
                for j in range(cols):
                    
                    next_number = (i * cols) + (j + 1)
                    new_bit = 1 - ((curr_bit & (1 << next_number)) == (1 << next_number))
                    next_bit = (curr_bit | (1<< next_number)) if new_bit else (curr_bit & ~(1<< next_number))
                    
                    for dir_x, dir_y in direction:
                        new_i, new_j = i + dir_x, j + dir_y
                        
                        if inbound(new_i, new_j):
                            next_number = (new_i * cols) + (new_j + 1)
                            
                            new_bit = 1 - ((next_bit & (1 << next_number)) == (1 << next_number))
                            next_bit = (next_bit | (1<< next_number)) if new_bit else (next_bit & ~(1<< next_number))
                    
                    
                    if next_bit not in visited:
                        visited.add(next_bit)
                        queue.append((next_bit, curr_step + 1))
        return -1
