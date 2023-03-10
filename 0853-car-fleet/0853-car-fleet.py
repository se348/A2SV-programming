class Solution:
    def calcMeetPos(self, elem1, elem2, target):
        if not (elem2[1] - elem1[1]):
            return (-1,-1)
        time = (elem1[0] - elem2[0]) / (elem2[1] - elem1[1])
        meet = elem1[0] + (elem1[1] * time)
        if meet > target or time < 0:
            return (-1, -1)
        if elem1[1] < elem2[1]:
            return elem1
        return elem2
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = list(zip(position, speed))
        arr.sort()
        stack = []
        for ind in range(len(arr)-1,-1,-1):
            i,j = arr[ind]
            if not stack:
                stack.append((i,j))
            else:
                prev = stack.pop()
                prev_new = self.calcMeetPos(prev, (i,j), target)
                if prev_new == (-1,-1):
                    stack.append(prev)
                    stack.append((i, j))
                else:
                    stack.append(prev_new)
        return len(stack)
        
        