class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        arrLen = min(arrLen, steps)
        
        
        curr = [0] * arrLen
        
        curr[0] = 1
        
        
        directions = [1, 0 , -1]
        inbound = lambda a : 0 <= a< arrLen
        
        for i in range(1, steps + 1):
            curr_copy = [0] * arrLen

            for j in range(arrLen):
                
                for a in directions:
                    if inbound(a + j):
                        curr_copy[j] += curr[a + j]
                        curr_copy[j] %= ((10 ** 9) + 7)
            curr = curr_copy
        return curr[0]