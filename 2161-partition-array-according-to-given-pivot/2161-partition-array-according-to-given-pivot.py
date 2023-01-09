class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        lessThanList = []
        greaterThanList = []
        equalList = []
        
        for num in nums:
            
            if num < pivot:
                lessThanList.append(num)
            
            elif num == pivot:
                equalList.append(pivot)
            
            else: 
                greaterThanList.append(num)
                
        arranged = []
        
        for num in lessThanList:
            arranged.append(num)
        
        for num in equalList:
            arranged.append(num)
            
        for num in greaterThanList:
            arranged.append(num)
            
        return arranged