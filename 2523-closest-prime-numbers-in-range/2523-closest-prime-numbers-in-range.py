class Solution:
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def checkPrime(num):
            for j in range(2, int(num** 0.5) + 1):
                if num % j == 0:
                    return False
                
            return True
        
        nums = []
        temp = []
        min_res= math.inf
        for i in range(max(left,2), right +1):
            if checkPrime(i):
                nums.append(i)
                
                if len(nums) >= 2:
                    if nums[-1] -nums[-2] < min_res:
                        min_res =nums[-1] -nums[-2]
                        temp = [nums[-2], nums[-1]]
                        if min_res <= 2:
                            return temp
                        
        if len(nums) <= 1:
            return [-1, -1]
        else:
            return temp
        
        