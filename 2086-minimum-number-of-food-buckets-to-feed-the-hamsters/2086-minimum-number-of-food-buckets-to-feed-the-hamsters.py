class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        
        pos = -2
        length = len(hamsters)
        count = 0
        
        for i in range(length):
            if hamsters[i] == ".":
                continue
            if pos + 1 == i:
                continue
                
            elif i != length -1:
                if hamsters[i + 1] == "H":
                    if i > 0 and hamsters[i - 1] == ".":
                        pos = i - 1
                        count += 1
                    else:
                        return -1
                else: 
                    pos = i + 1
                    count += 1
            elif i > 0 and hamsters[i - 1] == ".":
                pos = i - 1
                count += 1
            else: 
                return -1
        return count
                            
        