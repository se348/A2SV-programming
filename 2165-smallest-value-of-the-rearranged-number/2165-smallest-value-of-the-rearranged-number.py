class Solution:
    def findFirstNonZeroDigit(self, nums):
        index= -1
        for i, dig in enumerate(nums):
            if dig != "0":
                index =i
                return index
        
    def smallestNumber(self, num: int) -> int:
        if num ==0:
            return 0
        string_version = list(str(num))
        
        if string_version[0] =="-":
            string_version = sorted(string_version[1:], reverse= True)
            return int("".join(string_version)) * -1
        
        string_version.sort()
        index = self.findFirstNonZeroDigit(string_version)
        
        if index == 0:
            return int("".join(string_version))
        
        string_version[index], string_version[0] =  string_version[0], string_version[index]
        return int("".join(string_version))
            