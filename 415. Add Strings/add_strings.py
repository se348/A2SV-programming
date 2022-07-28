class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1 = num1[::-1]
        nums2 = num2[::-1]
        total=""
        rem = 0
        i=0
        while i < min(len(nums1), len(nums2)):
            curr_sum= int(nums1[i])+ int(nums2[i]) + rem
            if curr_sum> 9:
                rem = int(str(curr_sum)[:-1])
                curr_sum = int(str(curr_sum)[-1])
            else:
                rem = 0
            total+= str(curr_sum)
            i+=1
        while i < len(nums1):
            curr_sum= int(nums1[i])+ rem
            if curr_sum> 9:
                rem = int(str(curr_sum)[:-1])
                curr_sum = int(str(curr_sum)[-1])
            else:
                rem = 0
            total+= str(curr_sum)
            i+=1
        while i <  len(nums2):
            curr_sum= int(nums2[i]) + rem
            if curr_sum> 9:
                rem = int(str(curr_sum)[:-1])
                curr_sum = int(str(curr_sum)[-1])
            else:
                rem = 0
            total+= str(curr_sum)
            i+=1
        if rem!=0:
            total += str(rem)
        return total[::-1]