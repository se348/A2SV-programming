class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr =  []
        
        for i in range(len(weights) - 1):
            arr.append(weights[i] + weights[i + 1])
            
        arr.sort()
        
        min_score =  0
        max_score =  0
        
        for i in range(k - 1):
            
            min_score += arr[i]
            max_score += arr[-1- i]    
        
        return max_score - min_score
        