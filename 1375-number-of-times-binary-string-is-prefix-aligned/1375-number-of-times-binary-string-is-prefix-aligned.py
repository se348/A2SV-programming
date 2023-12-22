class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        visited = set()
        inital = 1
        answer = 0
        for i in range(len(flips)):

            visited.add(flips[i])
            if inital in visited:
            

                while inital in visited:
                    inital += 1
                
                answer += inital == i+2
                
        
        return answer
        

        
            