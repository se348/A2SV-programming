class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        defeats= collections.defaultdict(int)
        wins= collections.defaultdict(int)
        for [i,j] in matches:
            defeats[j]+=1
            wins[i]+=1
        
        never_lost=set()
        lost_once= set()
        for i, j in defeats.items():
            if j==1:
                lost_once.add(i)
        for i,j in wins.items():
            if defeats[i]==0:
                never_lost.add(i)
        return [sorted(list(never_lost)),sorted(list(lost_once))]
        