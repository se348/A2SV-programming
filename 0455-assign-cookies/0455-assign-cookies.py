class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        right = 0
        count = 0
        
        for left in range(len(g)):
            
            
            while right < len(s) and s[right] < g[left]:
                right += 1
            
            if right != len(s) and s[right] >= g[left]: 
                count += 1
                right += 1
        return count