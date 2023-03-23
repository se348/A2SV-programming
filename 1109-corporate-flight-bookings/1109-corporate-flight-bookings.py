from itertools import accumulate

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)
        
        for first, last, booking in bookings:
            answer[first -1] += booking
            answer[last] -= booking
            
        temp = list(accumulate(answer))    
        temp.pop()
        
        return temp