class Solution:
    def checkArithmeticSubarrays(self, nums: list, l: list, r: list) -> list:
        output =[True] * len(l)
        i=0
        while i< len(r):
            tempo= nums[l[i]: r[i]+ 1]
            tempo.sort()
            j=0
            while j< len(tempo)-2:
                if tempo[j+1] - tempo[j]!= tempo[j+2] -tempo[j+1]:
                   output[i] = False
                   break
                else:
                    j+=1
            i+=1
        return output
        

print( Solution().checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))