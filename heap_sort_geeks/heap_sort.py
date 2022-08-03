class Solution:
    def getLeftChild(self, i):
        l = 2 * i + 1
        return l
    def getRightChild(self,i):
        r =2 *i+2
        return r

    def heapify(self,arr, n, i):
        l = self.getLeftChild(i)
        r =self.getRightChild(i)
        if l>=n: return
        if l<n and r>=n  and arr[l] > arr[i]:
            arr[l], arr[i] = arr[i], arr[l]
            return self.heapify(arr,n, l)
        elif l<n and r>=n  and arr[l] <= arr[i]:
            return
        elif r<n and arr[r]>= arr[l] and arr[r] > arr[i]:
            arr[r], arr[i] = arr[i], arr[r]
            return self.heapify(arr,n, r)
        elif arr[l]> arr[r] and arr[l] > arr[i]:
            arr[l], arr[i] = arr[i], arr[l]
            return self.heapify(arr,n, l)
        elif arr[i] >= arr[r] and arr[i] >= arr[l]:
            return
        
    def buildHeap(self, arr,n):
        for i in range(n-1,-1,-1):
            self.heapify(arr, n,i)
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1,-1,-1):
            arr[0], arr[i]= arr[i], arr[0]
            self.heapify(arr, i, 0)
arr = [4,1,3,9,7]


a ="932 66 777 426 127 404 63 281 426 317 735 628 543 78 31 811 626 104 389 412 687 296 35 252 441 675 604 770 342 284 917 274 702 46 53 829 450 116 463 229 786 198 857 329 276 888 140 254 992 530 18 31 178 405 284 619 80 240 742 423 876 659 49 931 57 102 760 859 571 575 88 357 773 945 38 401 186 531 655 530 413 673 562 591 79 198 563 159 790 305 582 666 316 984 597 373 86 710 584 9 285 673 718 411 970 757 812 508 288 468 39 701 493 953 644 924 151 559 84 293 864 18 959 532 2 909 257 441 619 842 802 256 515 521 667 837 630 832 346 918 652 385 971 145 690 967"
lista =a.split()
for i,a in enumerate(lista):
    lista[i] =int(a)
s =Solution()
s.HeapSort(lista, len(lista))
print(lista)