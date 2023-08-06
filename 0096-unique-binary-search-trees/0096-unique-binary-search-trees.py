class Solution:
    def numTrees(self, n: int) -> int:
        arr = [1] * (n + 1)
        
        for i in range(2, n + 1):
            temp = 0
            for j in range(1, i + 1):
                left = j - 1
                right = i- j
                temp += arr[left] * arr[right]
            arr[i] = temp
        return arr[n]
        