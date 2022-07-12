from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i= 0
        j =len(people)-1
        count=0
        while i<= j:
            if i==j:
                count+=1
                break
            if people[j] == limit:
                count+=1
                j-=1
                continue
            if people[i] + people[j] > limit:
                j-=1
                count+=1
                continue
            if people[i] + people[j] <= limit:
                i+=1
                j-=1
                count+=1
                continue
        return count
    

s= Solution()
a = s.numRescueBoats([2,1], 3)
print(a)