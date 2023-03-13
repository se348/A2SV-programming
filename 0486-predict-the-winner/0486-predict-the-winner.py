class Solution:
    def predict(self, nums, left , right, turn):
        if left == right:
            if not turn:
                return [nums[left], 0]
            return [0,nums[left]]
        
        choice1 = self.predict(nums, left + 1, right, 1 - turn)
        choice1[turn] += nums[left]
        
        choice2 = self.predict(nums, left, right - 1, 1- turn)
        choice2[turn] += nums[right]
        
        if not turn: 
            return [max(choice1[0],  choice2[0]), min(choice1[1], choice2[1])]
        return [min(choice1[0],  choice2[0]), max(choice1[1], choice2[1])]
            
    def PredictTheWinner(self, nums: List[int]) -> bool:
        temp = self.predict(nums, 0, len(nums) - 1, 0)
        if temp[0] >= temp[1]:
            return True
        return False