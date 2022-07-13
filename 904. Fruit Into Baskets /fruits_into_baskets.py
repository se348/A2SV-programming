from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        answer= 0
        dictionary = {}
        i=0 
        for j in range(len(fruits)):
            if len(dictionary.keys())< 2 or fruits[j] in dictionary:
                if fruits[j] in dictionary:
                    dictionary[fruits[j]] +=1
                else:
                    dictionary[fruits[j]] =1
            else:
                while len(dictionary.keys()) ==2:
                    if dictionary[fruits[i]]>1:
                        dictionary[fruits[i]]-=1
                    else:
                        dictionary.pop(fruits[i])
                    i+=1
                if fruits[j] in dictionary:
                    dictionary[fruits[j]] +=1
                else:
                    dictionary[fruits[j]] =1
            print(dictionary,j)
            answer= max(answer, j-i+1)
        return answer
                        

            
s= Solution()
a= s.totalFruit([1,0,2,3,2,4,3,4,4,3,4,2,1,3,2])
print(a)