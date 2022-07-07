class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue =list(range(1,n+1))
        pointer = 0
        if n == 1:
            return 1
        round = 0
        cur_index = 0
        while len(queue) > 1:
            round +=1
            cur_index = (cur_index + k - 1)%len(queue)
            queue.pop(cur_index)
        return queue[0]

s = Solution()
a = s.findTheWinner(6, 5)
print(a)