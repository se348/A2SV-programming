class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        temp = []
        
        for i in range(len(nums)):
            temp.append((nums[i], i))
            
        temp.sort()
        marked_indexes = set()
        result = 0
        
        for i in range(len(temp)):
            
            if temp[i][1] not in marked_indexes:
                marked_indexes.add(temp[i][1] + 1)
                marked_indexes.add(temp[i][1] - 1)
                marked_indexes.add(temp[i][1])
                
                result += temp[i][0]
                
        return result
                
                