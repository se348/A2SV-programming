# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(curr, path):
            if not curr.left and not curr.right:
                path.append(f"{curr.val}")
                res.append("".join(path))
                return
            
            curr_path = path + [f"{curr.val}", "->"] 
            
            if curr.left:
                dfs(curr.left, curr_path[:])
            if curr.right:
                dfs(curr.right, curr_path[:])
        
        dfs(root, [])
        return res