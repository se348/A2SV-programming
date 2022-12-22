# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo={}
        def dfs(curr, robbed= False):
            if not curr:
                return 0
            if (id(curr), robbed) in memo:
                return memo[(id(curr), robbed)]
            elif robbed==True:
                a= dfs(curr.left, False)
                b= dfs(curr.right, False)
                memo[(id(curr), True)]= a+b
                return a+b
            else:
                a= dfs(curr.left, True)
                b= dfs(curr.right, True)
                
                c= dfs(curr.left, False)
                d= dfs(curr.right, False)
                memo[(id(curr), False)]= (max(a+b+curr.val,c+d))
                return(max(a+b+curr.val,c+d))
        first= TreeNode(0, root)
        return dfs(first)