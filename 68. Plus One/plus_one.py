from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringo =""
        for n in digits:
            stringo+= str(n)
        stringo = str(int(stringo)+1)
        return "".join(stringo)