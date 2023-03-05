class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for log in logs:
            if log == "../":
                count -= 1
                count= max(count, 0)
            elif log == "./":
                continue
            else:
                count += 1
                
        return count