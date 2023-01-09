# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, llist):
            if not root:
                return
            llist.append(root.val)
            dfs(root.left, llist)
            dfs(root.right, llist)
        
        llist = []
        dfs(root, llist)
        return llist
        