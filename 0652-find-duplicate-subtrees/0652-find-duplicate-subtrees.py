# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        counter = defaultdict(int)
        res = []
        def dfs(curr_node):
            if not curr_node:
                return "None"
            
            
            repr = f"{curr_node.val}--{dfs(curr_node.left)}-{dfs(curr_node.right)}"
            
            if counter[repr] == 1:
                res.append(curr_node)
            counter[repr] += 1
            return repr
        
        dfs(root)
        return res