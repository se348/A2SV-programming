class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        times = inf
        for ghost in ghosts:
            temp = abs(target[1] - ghost[1]) + abs(target[0] - ghost[0])
            times = min(temp, times)
            
        mine = abs(target[1] - 0) + abs(target[0] - 0)
        
        if mine < times:
            return True
        return False
        