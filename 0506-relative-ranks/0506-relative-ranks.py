class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        maxHeap = []
        for i in range(len(score)):
            curr = score[i]
            heappush(maxHeap, (-curr, i))
        
        result = [""] * len(score)
        b = 1
        
        while maxHeap:
            pos = heappop(maxHeap)[1]
            if b == 1:
                rank = "Gold Medal"
            elif b == 2:
                rank = "Silver Medal"
            elif b == 3:
                rank = "Bronze Medal"
            else :
                rank = str(b)
            
            result[pos] = rank
            b +=1
            
        return result