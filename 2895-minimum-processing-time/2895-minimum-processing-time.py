class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort()
        processorTime.sort()
        max_time = 0
        
        for i in range(len(processorTime)):
            max_time = max(max_time , processorTime[i]+tasks[-(4*i+1)])
        return max_time