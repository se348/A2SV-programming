class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        onesIndex = []
        
        for idx in range(len(boxes)):
            
            if boxes[idx] == "1":
                onesIndex.append(idx)
                
        operations = []
        
        for idx in range(len(boxes)):
            min_op = 0
            for one in onesIndex:
                min_op += abs(one -idx)
            
            operations.append(min_op)
            
        return operations