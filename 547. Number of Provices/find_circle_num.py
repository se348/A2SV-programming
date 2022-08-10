from typing import List


class Solution:
    all_set= set()
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        def dfs(curr,isConnected):
            self.all_set.remove(curr)
            for i in range(len(isConnected)):
                if isConnected[curr][i] ==1 and i in self.all_set:
                    dfs(i,isConnected)
        self.all_set = set(range(len(isConnected)))
        count=0
        while self.all_set:
            count+=1
            llist =list(self.all_set)
            dfs(llist[0], isConnected)
        return count