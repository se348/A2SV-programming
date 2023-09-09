class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        ver1_splitted, ver2_splitted = version1.split("."), version2.split(".")
        len_ver1, len_ver2 = len(ver1_splitted), len(ver2_splitted)
        min_length = min(len_ver1, len_ver2)
        
        for i in range(min_length):
            num1, num2 = int(ver1_splitted[i]), int(ver2_splitted[i])
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        for i in range(min_length, len_ver1):
            if int(ver1_splitted[i]) != 0:
                return 1
        
        for i in range(min_length, len_ver2):
            if int(ver2_splitted[i]) != 0:
                return -1
            
        return 0
        
        