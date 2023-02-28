class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i in range(len(tickets)):
            if i == k:
                q.append((tickets[i], True))
            else:
                q.append((tickets[i], False))
        
        count =0
        
        while q:
            if q[0][1] and q[0][0] == 1:
                return count +1  
            
            temp, isK = q.popleft()
            if temp != 1:
                q.append((temp -1 , isK))
            count += 1
            
        return 0
        