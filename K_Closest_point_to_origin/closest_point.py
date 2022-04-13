class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        for point in points:
            point.append(point[0]**2 + point[1] **2)
        Solution.mergeSort(points)
        points =points[:k]
        for point in points:
            point.pop()
        return points
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            Solution.mergeSort(L)
            Solution.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][2] < R[j][2]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    

s= Solution()
d =s.kClosest([[1,3],[-2,2]], 1)