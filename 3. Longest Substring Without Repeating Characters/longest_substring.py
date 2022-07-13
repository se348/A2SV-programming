class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        answer = 0
        my_set = set()
        for right_pointer in range(len(s)):
            while s[right_pointer] in my_set:
                my_set.remove(s[left_pointer])
                left_pointer+=1
            my_set.add(s[right_pointer])
            if right_pointer - left_pointer + 1> answer:
                answer = right_pointer - left_pointer + 1
        return answer