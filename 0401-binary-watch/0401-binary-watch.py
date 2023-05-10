class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        hours_and_mins = ['0'] * 10
        
        def dfs(curr_ind, count):
            curr_hrs = int("".join(hours_and_mins[:4]), 2)
            curr_mins =int("".join(hours_and_mins[4:]), 2)
            if curr_hrs >=12 or curr_mins >=60:
                return
            if count == turnedOn:
                if(len(str(curr_mins)) == 1):
                    ans.append(f'{curr_hrs}:0{curr_mins}')
                else:
                    ans.append(f'{curr_hrs}:{curr_mins}')
                return
            
            for i in range(curr_ind + 1, 10):
                hours_and_mins[i] = '1'
                dfs(i, count + 1)
                hours_and_mins[i] = '0'
        
        dfs(-1, 0)
        return ans
        