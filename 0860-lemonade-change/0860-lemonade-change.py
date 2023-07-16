class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        counter = defaultdict(int)
        
        for bill in bills:
            counter[bill] += 1
            
            if bill == 5:
                continue
                
            if bill == 10:
                if counter[5] == 0:
                    return False
                
                counter[5] -= 1
            
            else:
                if counter[10] >= 1 and counter[5] >= 1:
                    counter[10] -= 1
                    counter[5] -= 1
                    
                elif counter[5] >= 3:
                    counter[5] -= 3
                
                else:
                    return False
        return True
                    