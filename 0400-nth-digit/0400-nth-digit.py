class Solution:
    def binarySearch(self, arr, n):
        left = 0
        right = 11
        
        res = 0
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] <= n :
                res =mid
                left = mid + 1
            
            else:
                right = mid - 1
                
        return res
        
    def findNthDigit(self, n: int) -> int:
        if n <=9:
            return n
        arr = [1]
        for i in range(11):
            arr.append(9 * (10 ** i) * (i + 1) + arr[-1])
        arr[0] = 0
        ind  = self.binarySearch(arr, n)
        
        diff = n - arr[ind]
        a = diff // (ind + 1)
        b = diff % (ind + 1)
        
        
        curr = (10** ind) + a        
        return int(str(curr)[b])
        