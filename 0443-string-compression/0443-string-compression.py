from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        tempo, tempo_count=None,1
        new_chars=[]
        i, j =0,1
        if len(chars)==1:
            new_chars.append(chars[i])
        while j< len(chars):
            if chars[i]!= chars[j] and j== len(chars)-1:
                if tempo_count==1:
                    new_chars.append(chars[i])
                else:
                    new_chars.append(chars[i])
                    new_chars.append(str(tempo_count))
                new_chars.append(chars[j])
                break
            if chars[i] == chars[j] and j== len(chars)-1:
                tempo_count+=1
                new_chars.append(chars[j])
                new_chars.append(str(tempo_count))
                break
            if chars[i] == chars[j]:
                j+=1
                tempo_count+=1
                continue
            if chars[i] != chars[j]:
                if tempo_count==1:
                    new_chars.append(chars[i])    
                else:
                    new_chars.append(chars[i])
                    new_chars.append(str(tempo_count))
                i=j
                j+=1
                tempo_count =1
        new_chars= "".join(new_chars)
        for i, j in enumerate(new_chars):
            chars[i] = j
        while(len(chars) != len(new_chars)):
            chars.pop()
        #return len(chars)

