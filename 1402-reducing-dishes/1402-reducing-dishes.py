class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        suffix_sum = [satisfaction[0]]
        
        length = len(satisfaction)
        for i in range(1, length):
            suffix_sum.append(suffix_sum[-1] + satisfaction[i])
        
        res = [satisfaction[0]]
        
        for i in range(1, length):
            res.append(suffix_sum[i - 1] + satisfaction[i] + res[-1])
        res.append(0)
        return max(res)
        