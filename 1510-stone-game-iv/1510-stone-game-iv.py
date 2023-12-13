class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        arr = []
        
        @cache
        def checkWinner(curr_number, alice_turn):
            if curr_number == 0:
                if alice_turn:
                    return False
                return True
            if curr_number < 0:
                if alice_turn:
                    return True
                return False
            
            res = True if not alice_turn else False
            
            for i in range(len(arr)):
                
                got = checkWinner(curr_number -arr[i], not alice_turn)
                
                if not alice_turn:
                    res = res and got
                    if not res:
                        return False
                else:
                    res = res or got
                    if res:
                        return True
            return res
    
        
        i = 1
        
        while i ** 2 <= n:
            arr.append(i ** 2)
            i += 1
            
        return checkWinner(n, True)