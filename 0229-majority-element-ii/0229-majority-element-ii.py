class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        countArr  = Counter(nums)
        
        res = []
        n= len(nums)
        
        for num, val in countArr.items():
            
            if val > n/3:
                res.append(num)
                
        return res