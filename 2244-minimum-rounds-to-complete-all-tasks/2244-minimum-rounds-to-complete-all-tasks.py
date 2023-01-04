class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        
        round_res = 0

        for key, value in count.items():
            
            if value % 3 == 0:
                round_res += value/3
                
            elif value>=2 and (value -2) % 3 ==0:
                round_res += ((value-2)//3) +1
            
            elif value>=4 and (value -4) % 3==0:
                round_res += ((value-4)//3) + 2
                
                
            elif value % 2 ==0:
                round_res += value
                
            elif value % 2== 0:
                round_res += value/2
            
            else:
                return -1
        return int(round_res)