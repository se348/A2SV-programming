class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendSet = set(deadends)
        
        curr= "0000"
        queue = deque([curr])
        visited = set([curr])
        count =0
        
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr in deadends:
                    continue
                if curr == target:
                    return count
                
                for ind, elem in enumerate(curr):
                    new_ch1 = curr[:ind] + str(int(elem) + 1)[-1] + curr[ind+ 1:] 
                    if new_ch1 not in visited:
                        visited.add(new_ch1)
                        queue.append(new_ch1)
                    
                    if int(elem) ==  0:
                        new_ch2 = curr[:ind] + '9' + curr[ind+ 1:] 
                    else:
                        new_ch2 = curr[:ind] + str(int(elem) - 1)[-1] + curr[ind+ 1:] 
                    if new_ch2 not in visited:
                        visited.add(new_ch2)
                        queue.append(new_ch2)
                        
                
            count += 1
        return -1