class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.winner = [0] * len(times)
        curr = defaultdict(int)
        curr_elem = 0
        
        for ind, person in enumerate(persons):
            curr[person] += 1
            
            if curr[person] >= curr[curr_elem]:
                curr_elem = person
                
            self.winner[ind] = curr_elem
        
        self.times = times
        print(self.winner)
        
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) -1
        
        res = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.times[mid] <= t:
                res = mid
                left = mid + 1
            
            else:
                right = mid -1
        
        return self.winner[res]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)