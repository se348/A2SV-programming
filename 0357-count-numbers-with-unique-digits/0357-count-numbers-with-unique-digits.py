class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count =0
        def dfs(arr):
            nonlocal count
            if len(arr) == n:
                count += 1
                return
            for i in range(0, 10):
                if i not in arr or (arr and arr[-1]==0 and i==0):
                    arr.append(i)
                    dfs(arr)
                    arr.pop()
        dfs([])
        return count