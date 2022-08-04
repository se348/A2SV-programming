class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dictionary = self.constructTable(key)
        decoded=""
        for n in message:
            if n == " ":
                decoded += " "
            else:
                decoded+= dictionary[n]
        return decoded
        
        
    def constructTable(self, key):
        dictionary= {}
        letters='abcdefghijklmnopqrstuvwxyz'
        i=-1
        for n in key:
            if n==" " or n in dictionary:
                continue
            i+=1
            dictionary[n] = letters[i]
        return dictionary