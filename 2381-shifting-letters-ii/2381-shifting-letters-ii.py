class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        change =[0 for i in range(len(s) + 1)]
        
        for start, end, direction in shifts:
            if direction == 1:
                change[start] += 1
                change[end + 1] -= 1
            else:
                change[start] -= 1
                change[end + 1] += 1
                
        curr = 0
        new_s = []
        for ind, new_char in enumerate(s):
            curr += change[ind]
            new_s.append(chr((curr+ord(new_char)-97) % 26 + 97))
        return "".join(new_s)
        