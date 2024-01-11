class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        occurances = {}
        res = []
        
        for key in names:
            if key not in occurances:
                occurances[key] = 1
                res.append(key)
            
            else:
                c = 1

                while f"{key}({c})" in occurances:
                    c += 1

                occurances[f"{key}({c})"] = 1
                res.append(f"{key}({c})")
        return res