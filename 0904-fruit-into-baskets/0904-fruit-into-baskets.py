class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dictionary = defaultdict(int)
        start = 0
        res = 0
        
        for end in range(len(fruits)):
            dictionary[fruits[end]] += 1
            
            # if len(dictionary) <= 2:
            #     continue
            
            while len(dictionary) > 2:
                dictionary[fruits[start]] -= 1
                
                if dictionary[fruits[start]] == 0:
                    del dictionary[fruits[start]]
                
                start +=1
            
            res = max(res, end - start +1)
        
        return res