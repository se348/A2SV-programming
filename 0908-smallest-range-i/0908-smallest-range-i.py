class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        smallest = min(nums)
        largest = max(nums)
        
        return max(largest - smallest - (2 * k), 0)