class Solution:
    def largestNumber(self, nums: list) -> str:
        new_nums =nums.copy()
        self.mergeSort(new_nums, 0, len(new_nums)-1)
        anothe_nums =""
        for n in new_nums:
            anothe_nums+= str(n)
        return str(int(anothe_nums))
    def custom_cmp(self, num1, num2):
        choice1 = str(num1) + str(num2)
        choice2 = str(num2) + str(num1)
        if int(choice1) < int(choice2):
            return False
        else:
            return True
    def merge(self,arr, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle
        L = [0] * (n1)
        R = [0] * (n2)
        for index in range(0, n1):
            L[index] = arr[left + index]
    
        for index2 in range(0, n2):
            R[index2] = arr[middle + 1 + index2]
    
        index = 0     
        index2 = 0     
        index3 = left     
    
        while index < n1 and index2 < n2:
            if self.custom_cmp(L[index],R[index2]):
                arr[index3] = L[index]
                index += 1
            else:
                arr[index3] = R[index2]
                index2 += 1
            index3 += 1
        while index < n1:
            arr[index3] = L[index]
            index += 1
            index3 += 1
        while index2 < n2:
            arr[index3] = R[index2]
            index2 += 1
            index3 += 1
    def mergeSort(self,arr, left, right):
        if left < right:
            middle = left+(right-left)//2
            self.mergeSort(arr, left, middle)
            self.mergeSort(arr, middle+1, right)
            self.merge(arr, left, middle, right)
    

s= Solution()
a = s.largestNumber([3,30,34,5,9])
print(a)