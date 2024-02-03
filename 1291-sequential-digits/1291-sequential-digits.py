class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        
        arr = []
        
        for i in range(1, 10):
            curr_num = i    
            
            for j in range(i + 1, 10):
                curr_num *= 10
                curr_num += j
                
                if low <= curr_num <= high:
                    arr.append(curr_num)
                elif curr_num >= high:
                    break
        arr.sort()
        return arr