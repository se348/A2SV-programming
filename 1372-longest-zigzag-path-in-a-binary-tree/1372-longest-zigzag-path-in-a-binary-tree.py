# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        @cache
        def dfs(node, choice = 2 ):
            nonlocal ans
            if not node:
                return 0
            
            if choice == 2:
                a = dfs(node.left, 0)
                b = dfs(node.right,1)
                dfs(node.left, 2)
                dfs(node. right, 2)
                ans =max(a + 1, b + 1, ans)
            elif choice == 1:
                a = dfs(node.left, 0)
                b = dfs(node.right, 2)
                ans = max(ans, a + 1)
                return a + 1
            elif choice == 0:
                a = dfs(node.right, 1)
                b = dfs(node.left , 2)
                ans = max(ans, a + 1)
                return a + 1
        dfs(root)
        return ans - 1