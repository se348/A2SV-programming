class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        replacement_finder = {}
        
        for index in range(len(operations)-1, -1,-1):
            replaced, replacer = operations[index]
            
            if replacer in replacement_finder:
                new_replacer = replacement_finder.pop(replacer)
                replacement_finder[replaced] = new_replacer
                
            else:
                replacement_finder[replaced] = replacer
                
        new_array = []
        
        for num in nums:
            
            if num in replacement_finder:
                new_array.append(replacement_finder[num])
                
            else:
                new_array.append(num)
        
        return new_array
