class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        largest = -inf
        min_heap = []
        min_length = 0
        res = [-inf, inf]
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            largest = max(largest, nums[i][0])
            
        min_length = len(nums)
            
        while min_heap and len(min_heap) == min_length :
            curr_diff = res[1] - res[0]
            
            popped_elem, popped_ind, popped_a = heapq.heappop(min_heap)
            
            if (largest - popped_elem) < curr_diff:
                res =  [popped_elem, largest]
                
            if popped_a + 1 < len(nums[popped_ind]):
                heapq.heappush(min_heap, (nums[popped_ind][popped_a + 1], popped_ind, popped_a + 1))
                largest = max(largest, nums[popped_ind][popped_a + 1])
        return res