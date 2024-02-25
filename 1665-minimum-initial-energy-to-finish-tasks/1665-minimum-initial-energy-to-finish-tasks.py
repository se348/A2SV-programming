class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        new_tasks= []
        #order of insertion is -gap, -minim, task
        
        for i in range(len(tasks)):
            new_tasks.append((-(tasks[i][1] - tasks[i][0]), - tasks[i][1], tasks[i][0]))
        
        new_tasks.sort()
        
        maxim= 0
        curr= 0
        
        for i in range(len(new_tasks)):
            curr_minim = -new_tasks[i][1]
            
            added = max(curr_minim - curr, 0)
            maxim += added
            
            if (curr > -new_tasks[i][1]):
                curr -= new_tasks[i][2]
            else:
                curr = - new_tasks[i][0]
            # print(maxim)
        
        return maxim
#     1- 7   6
#     2- 8   6
#     3- 9   6
#     4-10   6
#     5-11   6
#     6-12   6    1
    
    
#     12- 6
#                         17
#         6