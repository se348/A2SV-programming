# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_d={}
        def dfs(root, level):
            if not root:
                return
            dfs(root.left, level+1)
            if level not in level_d:
                level_d[level] = [root.val]
            else:
                level_d[level].append(root.val)
            dfs(root.right,level+1)
        dfs(root, 0)
        keys = list(level_d.keys())
        keys.sort()
        ans=[]
        for i in keys:
            tempo = level_d[i]
            ans.append(sum(tempo)/len(tempo))
        return ans 