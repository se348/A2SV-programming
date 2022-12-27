class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        in_comment = False
        block_comment = False
        inline_comment = False
        res = []
        comment_started_line=0
        for i, word in enumerate(source):
            curr = ""
            index = 0
            change= False
            while index <len(word):
                if not in_comment and word[index]=="/" and index<len(word)-1 and word[index+1]=="*":
                    block_comment = True
                    in_comment= True
                    index+=2
                    comment_started_line = i
                elif not in_comment and word[index]=="/" and index<len(word)-1 and word[index+1]=="/":
                    in_comment = True
                    inline_comment = True
                    index+=2
                    
                elif block_comment and word[index] == "*" and index<len(word)-1 and word[index+1]=="/":
                    block_comment = False
                    in_comment = False
                    index += 2
                    change = True
                    
                elif not in_comment and res and change and comment_started_line != i:
                    res[-1] += word[index]
                    index += 1
                    
                elif not in_comment:
                    curr += word[index]
                    index+=1
                
                else:
                    index+=1
                    
            if curr:
                res.append(curr)    
                
            if inline_comment:
                inline_comment=False
                in_comment = False
        
        return res