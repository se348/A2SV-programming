class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        arr= [inf] * n
        arr[src] = 0
        
        for i in range(k + 1):
            old = arr.copy()
            for a, b, c in flights:
                arr[b] = min(old[b], old[a] + c, arr[b])
        return arr[dst] if arr[dst] != inf else -1
                
                