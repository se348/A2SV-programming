class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        queue = deque()
        queue.append((0,0))
        visited ={(0, 0 )}
        
        while queue:
            jog1, jog2 = queue.popleft()
            if jog1 == targetCapacity or jog2 == targetCapacity or jog1 + jog2 == targetCapacity:
                return True
            
            neighbors =[(0, jog2),(jog1, 0), (jug1Capacity, jog2), (jog1, jug2Capacity)]
            for n1, n2 in neighbors:
                if (n1, n2) not in visited:
                    visited.add((n1, n2))
                    queue.append((n1, n2))
            
            change = min(jug1Capacity - jog1, jog2)
            newjog1 = jog1 + change
            newjog2 = jog2 - change
            
            if (newjog1, newjog2) not in visited:
                visited.add((newjog1, newjog2))
                queue.append((newjog1, newjog2))
                
            change = min(jug2Capacity - jog2, jog1)
            newjog2 = jog2 + change
            newjog1 = jog1 - change
            
            if (newjog1, newjog2) not in visited:
                visited.add((newjog1, newjog2))
                queue.append((newjog1, newjog2))
                
        return False
                
            