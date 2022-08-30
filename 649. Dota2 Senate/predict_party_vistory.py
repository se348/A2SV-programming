class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qRadiant= []
        qDire=[]
        for i in range(len(senate)):
            if senate[i]=="R":
                qRadiant.append(i)
            else: qDire.append(i)
        while qRadiant and qDire:
            indRadiant = qRadiant.pop(0)
            indDire = qDire.pop(0)
            if (indRadiant< indDire):
                qRadiant.append(indRadiant + len(senate))
            else:
                qDire.append(indDire + len(senate))
        if qRadiant!=[]:
            return 'Radiant'
        return "Dire"