class Solution:
    # "(((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((()((**(**)()"
    #  12345 67890 12  345 4 5678  76 5 4321098767
    #       1     2  34   5 6    78  9 0
    def checkValidString(self, s: str) -> bool:

        extremes =  [0, 0]
        
        for char in s:
            
            if char == "(":
                extremes[0] += 1
                extremes[1] += 1
            
            elif char == ")":
                extremes[0] = max(0, extremes[0] - 1)
                extremes[1] -= 1
                
                if extremes[1] < 0:
                    return False
            
            else:
                extremes[0] = max(0, extremes[0] - 1)
                
                extremes[1] += 1
        
        return extremes[0] <= 0 <= extremes[1]        
                
