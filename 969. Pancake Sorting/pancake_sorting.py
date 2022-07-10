from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans =[]
        for i in range(len(arr)-1,0,-1):
            maximum_index, cond =self.findmax(arr, i)
            if cond ==1:
                self.flip(arr, maximum_index)
                ans.append(maximum_index+1)
            self.flip(arr, i)
            ans.append(i+1)
        return ans
    def findmax(self, arr, i):
        for j in range(1, i+1):
            if arr[j] == i+1:
                return j,1
        return None , 0
    def flip(self,arr, index):
        till =index//2
        for i in range(0, till+1):
            arr[i], arr[index- i] =arr[index -i] , arr[i]

s= Solution()
a = s.pancakeSort([3,2,4,1])
print(a)