from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        new_arr= []
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<= nums2[j]:
                new_arr.append(nums1[i])
                i+=1
            else:
                new_arr.append(nums2[j])
                j+=1
        while i< len(nums1):
            new_arr.append(nums1[i])
            i+=1
        while j< len(nums2):
            new_arr.append(nums2[j])
            j+=1
        if len(new_arr) %2==1:
            return new_arr[len(new_arr)//2]
        else:
            return (new_arr[len(new_arr)//2] + new_arr[(len(new_arr)//2)-1])/2