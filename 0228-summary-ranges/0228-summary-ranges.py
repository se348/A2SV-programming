class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return 
        
        curr_start, curr_end = None, None
        n = len(nums)
        arr = []
        
        for i in range(n):
            if curr_start == None:
                curr_start = nums[i]
                curr_end = nums[i]
            elif nums[i] == curr_end + 1:
                curr_end = nums[i]
            else:
                if curr_start == curr_end:
                    arr.append(str(curr_start))
                else:
                    arr.append(f"{curr_start}->{curr_end}")
                curr_start = nums[i]
                curr_end = nums[i]
        
        if curr_start == curr_end:
            arr.append(str(curr_start))
        else:
            arr.append(f"{curr_start}->{curr_end}")
        
        return arr