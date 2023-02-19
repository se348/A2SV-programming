class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        
        for i in range(n - 1):
            temp = []
            cur_val = None
            count = 0
            
            for j in range(len(curr)):
                
                if cur_val and cur_val == curr[j]:
                    count += 1
                
                elif cur_val and cur_val != curr[j]:
                    
                    temp.append(f"{count}{cur_val}")
                    cur_val = curr[j]
                    count = 1
                
                else:
                    cur_val = curr[j]
                    count = 1
            temp.append(f"{count}{cur_val}")
            curr = "".join(temp)
        
        return curr