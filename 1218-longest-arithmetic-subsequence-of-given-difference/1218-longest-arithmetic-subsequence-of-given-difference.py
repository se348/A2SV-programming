class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        elementToValueMapping = {}
        n= len(arr)
        result = [1] * n
        
        for i in range(n -1, -1, -1):
            
            next_value = arr[i] + difference
            if next_value in elementToValueMapping:
                result[i] = result[elementToValueMapping[next_value]] + 1
            
            elementToValueMapping[arr[i]] = i
            
        return max(result)