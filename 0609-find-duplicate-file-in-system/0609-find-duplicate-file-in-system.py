class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        llist = defaultdict(list)
        
        for path in paths:
            directories = path.split(" ")   
            root = directories[0]
            files = directories[1:]
            for file in files:
                exact_file, content = file.split("(")
                content = content[:-1]
                llist[content].append(root+"/"+ exact_file)
        
        res = []
        for content,values in llist.items():
            if len(values) > 1:
                res.append(values)
        
        return res
            