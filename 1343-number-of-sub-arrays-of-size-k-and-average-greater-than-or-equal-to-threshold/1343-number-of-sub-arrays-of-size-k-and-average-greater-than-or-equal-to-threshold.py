class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = 0
        
        total = sum(arr[:k])
        
        if total / k >= threshold:
            
            count += 1
        
        left = 0
        
        for right in range(k, len(arr)):
            
            total += arr[right]
            total -= arr[left]
            
            if (total / k) >= threshold:
                
                count += 1
            
            left += 1
        
        return count
            
            
            