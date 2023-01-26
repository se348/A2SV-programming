class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        left = 0
        right = len(people) -1
        
        boats = 0
        people.sort()
        
        while left < right:
            tempo = people[left] + people[right]
            
            if tempo <= limit:
                boats += 1
                left += 1
                right -= 1
                
            else:
                right -= 1
                boats += 1
            
        if left == right:
            boats += 1
        return boats