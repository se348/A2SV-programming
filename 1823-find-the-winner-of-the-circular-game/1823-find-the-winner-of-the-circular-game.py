class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque(range(1,n+1))
        
        curr = k
        
        while len(queue) != 1:
            val = queue.popleft()
            if curr != 1:
                queue.append(val)
                curr -= 1
            else:
                curr = k
        return queue[0]