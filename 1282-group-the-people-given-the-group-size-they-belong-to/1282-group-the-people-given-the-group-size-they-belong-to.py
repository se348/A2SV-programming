class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        same_size = defaultdict(list)
        n = len(groupSizes)
        
        for i in range(n):
            same_size[groupSizes[i]].append(i)
            
        res= []
        for key in same_size:
            groups = len(same_size[key]) // key
            
            count =0
            for i in range(groups):
                temp = []
                for j in range(key):
                    temp.append(same_size[key][count])
                    count += 1
                res.append(temp)
        return res
