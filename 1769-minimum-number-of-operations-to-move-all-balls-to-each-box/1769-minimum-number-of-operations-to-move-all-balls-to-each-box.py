class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        leftTraversal = [0 for _ in range(len(boxes))]
        rightTraversal =[0 for _ in range(len(boxes))]
        quantity = 0
        
        for idx, num in enumerate(boxes):
            
            if idx == 0:
                quantity += int(num)
                continue
            
            leftTraversal[idx] = leftTraversal[idx -1] + quantity
            quantity += int(num)
            
        quantity = 0
        
        for idx in range(len(boxes)-1,-1,-1):
            num = boxes[idx]
            
            if idx == len(boxes) - 1:
                
                quantity += int(num)
                continue
            
            rightTraversal[idx] = rightTraversal[idx +1] + quantity
            quantity += int(num)

        res = []
        
        for idx in range(len(rightTraversal)):
            res.append(rightTraversal[idx] + leftTraversal[idx])
            
        return res