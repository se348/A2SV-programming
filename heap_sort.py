class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,heap, n, current):

        largest_child = current
        left = 2 * current + 1
        right = 2 * current + 2
   
        if left < n and heap[left] > heap[largest_child]:
            largest_child = left
           
        if right < n and heap[right] > heap[largest_child]:
            largest_child = right
               
        if largest_child != current:
            heap[current], heap[largest_child] = heap[largest_child], heap[current]
            self.heapify(heap,n,largest_child)

    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        
        for i in range(n//2, -1,-1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n -1, -1,-1):
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
