
class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        index_list =[]
        result =[]
        for n in nums1:
            index_list.append(nums2.index(n))
        for k in index_list:
            g = nums2[k]
            condition =0
            for j in range(k, len(nums2)):
                if nums2[j] > g:
                    result.append(nums2[j])
                    condition=1
                    break
            if condition ==0:
                result.append(-1)
        return result
s= Solution()
a =s.nextGreaterElement([3,1,5,7,9,2,6],[1,2,3,5,6,7,9,11]  )
print(a)