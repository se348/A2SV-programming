class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        pairs = len(skill) //2
        
        if sum(skill) % pairs != 0:
            return -1
        
        skill.sort()
        
        left= 0
        right = len(skill) - 1
        initial = skill[left] + skill[right]        
        computed = 0

        while left <right:
            if skill[left] + skill[right] != initial:
                return -1
            computed += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return computed