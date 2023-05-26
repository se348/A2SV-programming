class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,1,0))
        visited = {(0,1)}
        
        while queue:
            curr_pos, curr_speed, curr_level = queue.popleft()
            
            if curr_pos == target:
                return curr_level
            
            next1_pos, next1_speed = curr_pos + curr_speed, curr_speed * 2
            next2_pos, next2_speed = curr_pos, - 1
            
            if next1_pos >= -1000 and next1_pos <= 3 * target and (next1_pos , next1_speed) not in visited:
                visited.add((next1_pos, next1_speed))
                queue.append((next1_pos, next1_speed, curr_level + 1))
                
            if next2_pos >= -1000:
                if curr_speed > 0:
                    if (next2_pos , next2_speed) not in visited:
                        visited.add((next2_pos, next2_speed))
                        queue.append((next2_pos, next2_speed, curr_level + 1))
                else:
                    if (next2_pos , 1) not in visited:
                        visited.add((next2_pos, 1))
                        queue.append((next2_pos, 1, curr_level + 1))
            