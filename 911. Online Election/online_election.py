from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times =times
        self.winner= []
        vote_count= {}
        vote_high= (persons[0], 1)
        for i in range(len(persons)):
            curr_vote =vote_count.get(persons[i],0) +1
            vote_count[persons[i]] =curr_vote
            if curr_vote >= vote_high[1]:
                vote_high =persons[i], curr_vote
            self.winner.append(vote_high[0])


    def q(self, t: int) -> int:
        low= 0 
        high=len(self.times)-1
        if t>= self.times[-1]:
            return self.winner[len(self.times)-1]
        result=-1
        while low<=high:
            mid =(low+high)//2
            if self.times[mid] ==t:
                return self.winner[mid]
            elif self.times[mid] > t:
                high= mid-1
            else:
                result =mid
                low= mid+1
        return self.winner[result]


t = TopVotedCandidate([0, 0, 1, 1, 2],[0, 67, 69, 74, 87])
print(t.q(100))