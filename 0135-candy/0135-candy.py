class Solution:
    def candy(self, ratings: List[int]) -> int:
        n= len(ratings)
        forward= [0] * n
        reverse = [0] * n
        
        forward[0] = 1
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                forward[i] = forward[i - 1] + 1
            else:
                forward[i] = 1
        
        reverse[n - 1] = 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                reverse[i] = reverse[i + 1] + 1
            else:
                reverse[i] = 1
                
        res = 0
        
        for i in range(n):
            res += max(forward[i] , reverse[i])
        
        return res