from decimal import Decimal as D
class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        
        maximum =1
        for i in range(len(points)):
            tempo = defaultdict(int)
            for j in range(len(points)):
                if j==i:
                    continue
                angle = math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])
                tempo[angle] += 1
            maximum = max(maximum, max(tempo.values())+ 1)
        return maximum
                    