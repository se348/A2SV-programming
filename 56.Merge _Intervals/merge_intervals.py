class Solution:
    
    def merge(self, intervals: list) -> list:
        self.sort_intervals(intervals)
        output=[intervals[0]]
        for p1, p2 in intervals[1:]:
            if output[-1][1]>=p1:
                temp =output[-1][1]
                output[-1][1] = max(p2,temp)
            else: 
                output.append([p1, p2])
        return output
        
    def sort_intervals(self, intervals):
        if len(intervals) > 1:
            mid = len(intervals)//2
            L = intervals[:mid]
            R = intervals[mid:]
            self.sort_intervals(L)
            self.sort_intervals(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][0] < R[j][0]:
                    intervals[k] = L[i]
                    i += 1
                else:
                    intervals[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                intervals[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                intervals[k] = R[j]
                j += 1
                k += 1
s= Solution()
d =s.merge([[1,4],[2,3]])
print(d)