class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        #[3,5,8,9,11,13,7,8,6] 4
        start = 0
        q = deque()
        count = 0
        
        for end in range(len(nums)):
            if nums[end] % 2==0:
                continue
                
            if len(q) == k:
                temp = q.popleft()
                if k ==1:
                    count += (temp - start + 1) * (end - temp)
                else:
                    count += (temp - start + 1) * (end - q[-1])
                start = temp + 1
            
            q.append(end)
            
        if len(q) == k:
            temp = q.popleft()
            if k == 1:
                count += (temp - start + 1) * (end - temp + 1)
            else:
                count += (temp - start + 1) * (end - q[-1] + 1)
            start = temp + 1
        
        return count
            