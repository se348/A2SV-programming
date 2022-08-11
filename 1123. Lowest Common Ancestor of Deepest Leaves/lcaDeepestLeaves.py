# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    depth=0
    ans= None
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def findDepth(curr,curr_depth=0):
            if curr and not curr.left and not curr.right:
                self.depth =max(self.depth, curr_depth)
            if curr.left:
                findDepth(curr.left, curr_depth+1)
            if curr.right:
                findDepth(curr.right, curr_depth+1)
        def dfs(curr, curr_depth=0):
            if curr and not curr.left and not curr.right:
                if curr_depth == self.depth:
                    if not self.ans:
                        self.ans= curr
                    return True
                return False
            elif curr.left and curr.right:
                l = dfs(curr.left, curr_depth+1)
                r= dfs(curr.right, curr_depth+1)
                if l and r:
                    self.ans = curr
                    return True
                elif l or r:
                    return True
                else:
                    return False
            elif curr.left:
                l = dfs(curr.left, curr_depth+1)
                if l:
                    return True
                return False
            elif curr.right:
                l = dfs(curr.right, curr_depth+1)
                if l:
                    return True
                return False
        findDepth(root)
        dfs(root)
        return self.ans

t= TreeNode(2)
c = TreeNode(3, None, t)
r= TreeNode(1)
g= TreeNode(0,r,c)

s= Solution()
q =s.lcaDeepestLeaves(g)
print(q.val)