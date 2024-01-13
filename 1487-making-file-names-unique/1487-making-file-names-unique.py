class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        
        occurances = {}
        res = []
        
        for key in names:
            if key not in occurances:
                occurances[key] =  1
                res.append(key)
                continue
                
            occurances[key] += 1
            
            while f"{key}({occurances[key] - 1})" in occurances:
                occurances[key] += 1
            occurances[f"{key}({occurances[key] - 1})"] = 1
            res.append(f"{key}({occurances[key] - 1})")
            
            
        return res