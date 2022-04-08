class Solution:
    def select(self, arr, i):
        smallest =arr[i]
        for j in range(i, len(arr)):
            if arr[j] < smallest:
                smallest =arr[j]
        arr[arr.index(smallest, i, len(arr))], arr[i] =arr[i], arr[arr.index(smallest, i, len(arr))] 
    def selectionSort(self, arr, n):
        for j in range(len(arr)):
            self.select(arr, j)