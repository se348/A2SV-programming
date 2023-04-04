class Solution:
    def partitionString(self, s: str) -> int:
        s_arr = [0] * 26
        count = 0
        
        for right in range(len(s)):
            curr = ord(s[right]) - ord('a')
            
            if s_arr[curr] != 0:
                count += 1
                s_arr = [0] * 26
            s_arr[curr] += 1
            
        return count + 1