class Solution:
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        temp = []
        
        for i in range(len(intervals)):
            temp.append((intervals[i][0], i))
        
        temp.sort()
        
        res = []
        
        
        for start, end in intervals:
            
            left  = 0            
            right = len(intervals) -1
            
            curr = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if temp[mid][0] >= end:
                    curr = temp[mid][1]
                    right = mid -1
                else:
                    left = mid + 1
                    
            res.append(curr)
        
        return res