class ATM:

    def __init__(self):
        self.curr_notes = [0] * 5
        
    def deposit(self, banknotesCount: List[int]) -> None:
        
        
        for i in range(5):
            self.curr_notes[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        
        result = [0] * 5
        values = [20, 50, 100, 200, 500]
        
        
        for i in range(len(values) - 1, -1, -1):
            
            curr_val = values[i]
            substraction = amount // curr_val
            
            if substraction > self.curr_notes[i]:
                
                result[i] =  self.curr_notes[i]
                amount -= (self.curr_notes[i] * values[i])
            
            elif substraction != 0:
                result[i] =  substraction
                amount -= (substraction * values[i])
        
        if amount != 0:
            return [-1]
        
        for i in range(5):
            self.curr_notes[i] -= result[i]
        
        return result
            
            
# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)