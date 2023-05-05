class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n +1):
            binary = bin(i)
            count = 0
            for j in range(2, len(binary)):
                if binary[j] == '1':
                    count += 1
            res.append(count)
        return res
                
        
        
        