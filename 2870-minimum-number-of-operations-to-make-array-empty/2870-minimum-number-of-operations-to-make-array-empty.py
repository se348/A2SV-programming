# 4 -> 0 * 3 + 2 * 2
# 7 -> 2 * 2 + 1 * 3
# 13-> 


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counted = Counter(nums)
        
        result = 0
        for key in counted:
            value = counted[key]
            
            
            if value == 1:
                return -1
            
            if value % 6 != 1:
                result += ((value // 6) * 2)
                value %= 6
                if value == 0:
                    continue
                elif 2 <= value <= 3:
                    result += 1
                else:
                    result += 2
            else:
                temp = value - 7
                result += ((temp // 6) * 2)
                result += 3
            
        return result