class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        failed =  set()
        
        for i in range(len(fronts)):
            
            if fronts[i] == backs[i]:
                failed.add(fronts[i])
                
        min_res= inf
        
        for i in range(len(fronts)):
            if fronts[i] != backs[i]:
                
                if fronts[i] not in failed:
                    min_res = min(fronts[i], min_res)
                
                if backs[i] not in failed:
                    min_res = min(backs[i], min_res)
        
        return min_res if min_res != inf else 0 