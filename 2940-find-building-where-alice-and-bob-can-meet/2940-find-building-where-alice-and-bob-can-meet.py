class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        query_dict = defaultdict(list)
        
        for ind in range(len(queries)):
            
            i, j = queries[ind]
            
            if j >= i:
                query_dict[j].append((i, ind))
            
            else:
                query_dict[i].append((j, ind))
        # print(query_dict)
        n = len(heights)
        res = [-1] * len(queries)
        
        monotonic_stack = []
        
        for i in range(n - 1, -1, -1):
            
            while monotonic_stack and heights[i] >= monotonic_stack[-1][0]:
                monotonic_stack.pop()
            
            monotonic_stack.append((heights[i], i))

            # print(monotonic_stack, i)
            for j in query_dict[i]:
                
                if j[0] == i:
                    res[j[1]] = i
                    continue
                
                
                left = 0
                right = len(monotonic_stack) - 1
                
                correct = -1
                # print(j)
                # print(monotoni)
                while left <= right:
                    mid = (left + right) // 2
                    
                    if monotonic_stack[mid][0] > heights[j[0]]:
                        correct= monotonic_stack[mid][1]
                        left = mid + 1
                    else:
                        right = mid - 1
                
                res[j[1]] = correct
                
        return res