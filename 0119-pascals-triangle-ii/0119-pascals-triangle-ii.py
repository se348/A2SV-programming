class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        tempo = self.getRow(rowIndex -1)
        res = [1]
        for i in range(len(tempo) -1):
            res.append(tempo[i] + tempo[i + 1])
        res.append(1)
        return res