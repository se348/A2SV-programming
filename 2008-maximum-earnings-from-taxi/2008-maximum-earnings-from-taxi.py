class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        rides.sort()
        n = len(rides)
        
        has_profit = [0] * n
        no_profit = [0] * n
        
        start_time = [a[0] for a in rides]
        end_time = [a[1] for a in rides]
        
        
        has_profit[-1] = rides[-1][1] -  rides[-1][0] + rides[-1][2]
 
        for i in range(n - 2, -1, -1):
            
            next_ind = bisect_left(start_time, end_time[i], lo= i+ 1)
            t =  (rides[i][1] - rides[i][0] + rides[i][2])

            if next_ind != n:
                
                has_profit[i] = no_profit[next_ind] + t
                has_profit[i] = max(has_profit[i], has_profit[next_ind] + t)
            
            has_profit[i] = max(has_profit[i], t)
            no_profit[i] = max(no_profit[i + 1], has_profit[i + 1])
            
        a, b= max(has_profit), max(no_profit)
        return max(a, b)
            
            
            
            
            