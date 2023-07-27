class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        arr = [0] * n
        
        for i in range(n -1, -1, -1):
            arr[i] = values[i] - i
            if i +1 < n:
                arr[i]= max(arr[i], arr[i + 1])
        
        res = [-inf] * n
        
        for i in range(n - 1):
             res[i] = values[i] + arr[i + 1] + i
        
        return max(res)