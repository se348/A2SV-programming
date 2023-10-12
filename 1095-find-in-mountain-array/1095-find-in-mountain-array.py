# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binarySearch(self, mountain_arr, left, right, target, reversed):
        
        while left <= right:
            mid = (left + right) // 2
            
            val = mountain_arr.get(mid)
            
            if val == target:
                return mid
            
            elif not reversed and val > target:
                right = mid - 1
            elif reversed and val > target:
                left = mid + 1
            elif reversed:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    
    def findLargestNumber(self, mountain_arr):
        length =mountain_arr.length()
        left = 0
        right = length - 1
        
        while left < right:
            mid = (left + right) // 2
            
            val_mid_plus_one = mountain_arr.get(mid + 1) if (mid + 1) < length else 0
            val_mid =  mountain_arr.get(mid) 
            val_mid_mius_one = mountain_arr.get(mid - 1) if mid - 1 >=0 else 0
            
            if val_mid_plus_one > val_mid >  val_mid_mius_one:
                left = mid + 1
            
            elif val_mid_plus_one < val_mid <  val_mid_mius_one:
                right = mid - 1
            
            else:
                return mid
        return left
        
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        largest_ind = self.findLargestNumber(mountain_arr)
        
        left=  0 
        res = self.binarySearch(mountain_arr, left, largest_ind, target, False)        
        if res != -1:
            return res
        return self.binarySearch(mountain_arr, largest_ind + 1, mountain_arr.length()- 1, target, True) 
                
        
        