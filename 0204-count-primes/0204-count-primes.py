class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        visited = set()
        count = 1
        
        for i in range(3, n):
            if i % 2 == 0:
                continue
            if i not in visited:
                count += 1
            else:
                continue
            curr = i * i
            while curr < n:
                visited.add(curr)
                curr += i
                
        
        return count