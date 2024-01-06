class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(endTime)
        ap = []
        
        for i in range(n):
            ap.append((startTime[i], profit[i], endTime[i]))
            
        ap.sort()
        
        startTime = [a[0] for a in ap]
        profit = [a[1] for a in ap]
        endTime = [a[2] for a in ap]

        has_profit = profit.copy()
        no_profit = [0] * n
        
        
        for i in range(n - 2, -1, -1):
            
            # For inclusion
            
            ind = bisect_left(startTime, endTime[i], lo=i+ 1)
            if (ind != n):
                has_profit[i] = max(has_profit[ind] + profit[i], has_profit[i])
                has_profit[i] = max(no_profit[ind] + profit[i], has_profit[i]) 
                
            # For Declusion
            no_profit[i] = no_profit[i + 1]
            no_profit[i] = max(has_profit[i + 1], no_profit[i])
            
        a, b = max(has_profit), max(no_profit)
        
        return max(a, b)