class Solution:
    def numberOfWays(self, corridor: str) -> int:
        number_of_seats = 0
        
        for typ in corridor:
            if typ == "S":
                number_of_seats += 1
                
        if (number_of_seats & 1) or not number_of_seats:
            return 0
        
        gaps = []
        last_seat = -1
        curr_seat_count = 0
        
        for i in range(len(corridor)):
            if corridor[i] == "S":
                if curr_seat_count % 2 == 0:
                    gaps.append(i - last_seat)
                else:
                    last_seat = i
                curr_seat_count += 1
        res = 1
        
        for i in range(1, len(gaps)):
            res = (res * gaps[i]) % (10 ** 9 + 7)
        
        return res