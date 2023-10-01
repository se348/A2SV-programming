class Solution:
    def binary_search(self, nums, value):
        left = 0
        right = len(nums) - 1
        
        closest = inf
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == value:
                return 0
            
            elif nums[mid] > value:
                closest = min(closest, nums[mid] - value)
                right = mid - 1
            else:
                closest = min(closest, value - nums[mid])
                left = mid + 1
        
        return closest
        
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        result = 0
        heaters.sort()
        
        for house in houses:
            result = max(result, self.binary_search(heaters, house))
            
        return result