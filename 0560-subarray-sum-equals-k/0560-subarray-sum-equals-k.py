class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] += 1
        
        curr = 0
        res = 0
        
        for elem in nums:
            curr += elem
            res += prefixSum[curr - k]
            prefixSum[curr] += 1
            
        return res
        