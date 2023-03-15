class Solution:
    def countGoodNumbers(self, n: int) -> int:
        memo ={0: 5, 1: 20}
        temp = bin(n) 
        
        arr_rep = []
        
        for i in range(2,len(temp)):
            arr_rep.append(temp[i])
        
        
        arr_rep.reverse()
        
        for i in range(2, len(arr_rep)):
            memo[i] = pow(memo[i-1], 2, 10 ** 9 + 7)

        res = 1
        
        for i in range(len(arr_rep)):
            if int(arr_rep[i]):
                res =(res * memo[i]) %( 10 **9 + 7)
        return res
        
        
        
        