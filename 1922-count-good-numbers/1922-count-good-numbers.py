class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n % 2 ==0:
            return int(pow(4, (n//2), (10** 9) + 7)  * pow(5,(n//2),(10**9)+7 ))% (10 **9 + 7)
        return int(pow(4, (n//2), 10 ** 9 +7)  * pow(5 ,((n//2) + 1),10**9+7))% (10 **9 + 7)
        
            
    