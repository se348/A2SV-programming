# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def findDepth(root,level):
            if not root:
                return level
            l = findDepth(root.left, level+1)
            r = findDepth(root.right, level+1)
            return max(l,r)
        def traverse(curr, level):
            if not curr:
                return
            ans[level].append(curr.val)
            traverse(curr.left, level+1)
            traverse(curr.right, level+1)
        max_depth = findDepth(root,0)
        for i in range(max_depth):
            ans.append([])
        traverse(root, 0)
        for i in range(len(ans)):
            if i%2==0:
                continue
            ans[i] = ans[i][::-1]
        return ans 