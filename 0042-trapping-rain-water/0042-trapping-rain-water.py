class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxim_reverse = [ 0 ] * n
        
        maxim_reverse[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            maxim_reverse[i] = max(maxim_reverse[i + 1], height[i])
        
        maxim = [ 0 ] * n
        maxim[0] = height[0]
        
        for i in range(1, n):
            maxim[i] = max(maxim[i - 1], height[i])
        
        res = 0
        
        for i in range(n):
            curr = min(maxim[i], maxim_reverse[i]) - height[i]
            res += curr
        
        return res