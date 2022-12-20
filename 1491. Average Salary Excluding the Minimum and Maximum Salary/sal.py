class Solution:
    def average(self, salary: List[int]) -> float:
        min_index= 0
        min_val= math.inf
        
        max_index= 0
        max_val= 0
        
        for i, sal in enumerate(salary):
            if sal< min_val:
                min_val =sal
                min_index=i
            if sal> max_val:
                max_val =sal
                max_index=i
        total =0
        for i in range(len(salary)):
            if i==min_index or i==max_index:
                continue
            total+= salary[i]
        return total/(len(salary)-2)