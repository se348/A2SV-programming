class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_length = len(ages)
        
        sorted = [(ages[i], scores[i]) for i in range(age_length)]
        sorted.sort()
        
        result = [0] * age_length
        
        for i in range(age_length - 1, -1, -1):
            curr_score = sorted[i][1]
            result[i]= curr_score
            for j in range(i + 1, age_length):
                if sorted[j][1] >= curr_score:
                    result[i] = max(result[i], result[j] + curr_score)
            
        return max(result) 