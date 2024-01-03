class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        count = 0
        prev  = 0
        
        for i in range(len(bank)):
            
            curr = 0
            
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    curr += 1
            
            count += (prev * curr)
            
            if curr != 0:
                prev = curr
        
        return count
                