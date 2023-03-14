class Solution:
    def reverse(self, arr: list):
        for i in range(len(arr)//2):
            arr[i] , arr[len(arr) -1 -i] = arr[len(arr) -1 -i], arr[i]
        return arr
    
    def invert(self, arr: list):
        new_arr = [0] * len(arr)
        for i in range(len(arr)):
            new_arr[i] = 1 - arr[i]
        return new_arr
    
    def logic(self, n: int):
        if n == 1:
            return [0]
        
        curr = self.logic(n- 1)
        temp = self.reverse(self.invert(curr))
        curr.append(1)
        curr.extend(temp)
        return curr
        
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.logic(n)[k - 1])
        
        