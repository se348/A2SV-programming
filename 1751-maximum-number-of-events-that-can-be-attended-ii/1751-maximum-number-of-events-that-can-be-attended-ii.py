class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()
        start_time = [a[0] - 1 for a in events]
        end_time = [a[1] for a in events]
        
        @cache
        def dfs(ind, visited, curr_k):
            if curr_k > k:
                return 0
            if ind >= len(events):
                return 0
            
            if visited:
                next_ind = bisect_left(start_time, end_time[ind], lo=ind + 1)
                opt = events[ind][2]
                
                a = dfs(next_ind, False, curr_k)
                b = dfs(next_ind, True, curr_k + 1)
                
                return max(opt + a, opt + b)
            
            opt1 = dfs(ind + 1, True, curr_k + 1)
            opt2 = dfs(ind + 1, False, curr_k)

            return max(opt1, opt2)

        return max(dfs(0, True, 1), dfs(0, False, 0))