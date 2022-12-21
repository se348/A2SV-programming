class Solution:
    def interpret(self, command: str) -> str:
        index =0 
        res=""
        while index<len(command):
            if command[index]=="G":
                res+="G"
                index+=1
            elif command[index]=="(" and index<len(command)-1 and command[index+1]==")":
                res+="o"
                index+=2
            elif command[index]=="(" and index<len(command)-3 and command[index+1:index+4]=="al)":
                res+="al"
                index+=4
        return res
                