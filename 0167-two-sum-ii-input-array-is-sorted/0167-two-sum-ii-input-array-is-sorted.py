class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1
        
        while left_ptr < right_ptr:
            total = numbers[left_ptr] + numbers[right_ptr]
            if total == target:
                return [left_ptr + 1, right_ptr + 1]
            elif total < target:
                left_ptr += 1
            else: right_ptr -=1
        return [0,1]