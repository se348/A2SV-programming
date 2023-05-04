class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        monotonic_queue = deque()
        
        result= []
        
        for i in range(len(nums)):
            while monotonic_queue and nums[i] > monotonic_queue[-1][0]:
                monotonic_queue.pop()
            monotonic_queue.append((nums[i], i))
            
            while i - monotonic_queue[0][1] >= k:
                monotonic_queue.popleft()
                
            result.append(monotonic_queue[0][0])
            
        return result[k - 1:]