class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        maxim_starting_from_index= defaultdict(int)
        
        for i in range(len(arr) - 1, -1, -1):
            curr_max = arr[i]
            
            for j in range(i, min(len(arr), i + k)):
                curr_max = max(arr[j], curr_max)
            
                maxim_starting_from_index[i] = max(maxim_starting_from_index[j + 1] + curr_max * (j - i + 1), maxim_starting_from_index[i])
                
        return maxim_starting_from_index[0]
    