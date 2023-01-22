class Solution:
    def leftMostBinarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        index = math.inf
        while left <= right:
            mid = ( left + right) // 2
            
            if nums[mid] == target:
                index = min(mid, index)
                right = mid - 1
            
            elif nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1
        return index
    def rightMostBinarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = ( left + right) // 2
            if nums[mid] == target:
                index = max(mid, index)
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return index
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        leftMost = self.leftMostBinarySearch(nums, target)
        rightMost = self.rightMostBinarySearch(nums, target)
        if rightMost == -1:
            return []
        return list(range(leftMost, rightMost + 1))
        