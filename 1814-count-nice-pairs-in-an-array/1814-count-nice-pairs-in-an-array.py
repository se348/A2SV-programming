class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        pairs = defaultdict(int)
        
        for i in range(len(nums)):
            
            curr_number = nums[i]
            reversed_number = int(str(curr_number)[::-1])
            
            pairs[curr_number - reversed_number] += 1
            
        res = 0

        for key in pairs:
            temp = pairs[key]
            
            res += (temp * (temp - 1)) // 2
            
        return res % (10 ** 9 + 7)