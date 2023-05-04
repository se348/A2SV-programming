class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        accumulator = 0
        
        for i in range(len(nums)):
            accumulator += nums[i]
            prefix.append(accumulator)
        
        monotonic_queue = deque()
        result = math.inf
        for i in range(len(prefix)):
            while monotonic_queue and monotonic_queue[-1][0] > prefix[i]:
                monotonic_queue.pop()
            monotonic_queue.append((prefix[i], i))
            
            while monotonic_queue and monotonic_queue[-1][0] - monotonic_queue[0][0] >= k:
                
                result = min(result, monotonic_queue[-1][1] - monotonic_queue[0][1])
                monotonic_queue.popleft()
                
        if result == math.inf:
            return -1
        return result