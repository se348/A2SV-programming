class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        visited = set()
        inital = 1
        answer = 0
        max_ = 0
        for i in range(len(flips)):

            visited.add(flips[i])
            max_ = max(flips[i],max_)
            if inital in visited:
                answer += (len(visited)==i+1) and (max_ == i+1)

                while inital in visited:
                    inital += 1
        
        return answer
        

        
            