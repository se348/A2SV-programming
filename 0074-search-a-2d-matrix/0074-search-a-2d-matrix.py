class Solution:
    def findRow(self, matrix, target):
        topPtr =0
        bottomPtr = len(matrix) - 1
        rowNumber = 0
        while topPtr <= bottomPtr:
            midPtr = (topPtr + bottomPtr) //2
            
            if matrix[midPtr][0] <= target:
                rowNumber = midPtr
                topPtr = midPtr + 1
                
            else:
                bottomPtr = midPtr - 1
        return rowNumber
            
    def binarySearch(self, arr, target):
        leftPtr = 0
        rightPtr = len(arr) -1
        
        while leftPtr <= rightPtr:
            midPtr = (leftPtr + rightPtr) //2
            if arr[midPtr] == target:
                return True
            elif arr[midPtr] < target:
                leftPtr = midPtr +1
            else:
                rightPtr = midPtr - 1
        
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
            val = self.findRow(matrix, target)

            return self.binarySearch(matrix[val], target)