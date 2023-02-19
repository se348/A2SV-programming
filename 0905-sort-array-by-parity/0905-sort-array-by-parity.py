class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenFinder= 0
        oddFinder = 1
        
        while oddFinder < len(nums):
            
            if nums[oddFinder] % 2 ==1:
                oddFinder += 1
            elif nums[evenFinder] % 2 ==0:
                evenFinder += 1
            else:
                nums[oddFinder] , nums[evenFinder] = nums[evenFinder], nums[oddFinder]
                oddFinder +=1
                evenFinder += 1
            if evenFinder ==oddFinder:
                oddFinder += 1
        return nums