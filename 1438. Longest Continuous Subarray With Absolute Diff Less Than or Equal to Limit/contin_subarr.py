
import collections
class Solution:
    def longestSubarray(self, nums: list, limit: int) -> int:
        fast_pointer=0
        slow_pointer =0
        largest =0
        min_queue =collections.deque([])
        max_queue =collections.deque([])
        while fast_pointer <len(nums):
            while min_queue and min_queue[-1] > nums[fast_pointer]:
                min_queue.pop()
            min_queue.append(nums[fast_pointer])
            while max_queue and max_queue[-1] < nums[fast_pointer]:
                max_queue.pop()
            max_queue.append(nums[fast_pointer])
            tempo= max_queue[0] - min_queue[0]
            length =fast_pointer -slow_pointer +1
            if tempo <= limit:
                if length> largest:
                    largest =length
            else:
                if max_queue[0] == nums[slow_pointer]:
                    max_queue.popleft()
                if min_queue[0] == nums[slow_pointer]:
                    min_queue.popleft()
                slow_pointer+=1
            fast_pointer+=1
        return largest
    
s= Solution()
d= s.longestSubarray([8,2,4,7],4)
print(d)