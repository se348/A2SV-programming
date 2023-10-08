# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left_most = defaultdict(lambda: inf)
        right_most = defaultdict(int)
        
        def dfs(curr_node,curr_layer, number):
            left_most[curr_layer] = min(left_most[curr_layer], number)
            right_most[curr_layer] = max(right_most[curr_layer], number)
            
            if curr_node.left:
                dfs(curr_node.left, curr_layer + 1, 2 * number + 1)
            
            if curr_node.right:
                dfs(curr_node.right, curr_layer + 1, 2 * number + 2 )
        
        dfs(root, 0, 0)
        
        result = 0
        
        for key in left_most:
            result =max(result, right_most[key] - left_most[key] + 1)
            
        return result