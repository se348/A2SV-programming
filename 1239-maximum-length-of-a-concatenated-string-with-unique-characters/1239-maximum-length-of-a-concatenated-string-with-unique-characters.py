class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        n= len(arr)
        maxim = 0
        
        for i in range(pow(2, n)):
            j = 1
            temp = set()
            cond = True    
            
            c= 0
            while j <= i:
                if j & i:
                    for a in arr[c]:
                        if a in temp:
                            cond = False
                            break
                        else:
                            temp.add(a)
                    if not cond:
                        break
                        
                c += 1
                j <<= 1
                
            if cond:
                maxim = max(maxim, len(temp))
        return maxim
                
                
                        
            
        