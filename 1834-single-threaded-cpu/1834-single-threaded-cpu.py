class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()
        min_heap  = [[tasks[0][1], tasks[0][2], tasks[0][0]]]
        curr_time = tasks[0][0]
        curr_index = 1
        result = []
        
        while min_heap:
            
            proccessing_time, index, available_time =heapq.heappop(min_heap)
            curr_time += proccessing_time
            result.append(index)
        
            while curr_index < len(tasks) and tasks[curr_index][0] <= curr_time:
                
                heapq.heappush(min_heap, (tasks[curr_index][1], tasks[curr_index][2], tasks[curr_index][0]))
                curr_index +=1
            
            if not min_heap and curr_index <len(tasks):
                heapq.heappush(min_heap, (tasks[curr_index][1], tasks[curr_index][2], tasks[curr_index][0]))
                curr_time = tasks[curr_index][0]
                curr_index +=1
        return  result

         