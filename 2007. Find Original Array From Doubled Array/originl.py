from collections import Counter


class Solution:
    def findOriginalArray(self, changed):
        length = len(changed)
        if (length % 2) != 0:
            return []

        unchanged = []
        count = Counter(changed)
        changed.sort() 
        
        for num in changed:
            if num == 0 and (count[num] % 2) != 0:
                return []

            if count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                unchanged.append(num)
        
        if len(unchanged) == length //2:
            return unchanged
        return []
