# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        
        
        def dfs(curr_node):
            if curr_node and not curr_node.left and not curr_node.right:
                return [curr_node.val, curr_node.val, 0]
            
            min_val, max_val, max_gap =  curr_node.val, curr_node.val, 0 
            
            if curr_node.left:
                left_min, left_max, left_gap = dfs(curr_node.left)
                
                max_gap = max(max_gap, left_gap, abs(left_max - curr_node.val), abs(left_min - curr_node.val))
                
                max_val = max(left_max, max_val)
                min_val = min(left_min, min_val)
                
            if curr_node.right:
                right_min, right_max, right_gap = dfs(curr_node.right)
                
                max_gap = max(max_gap, right_gap, abs(right_max - curr_node.val), abs(right_min - curr_node.val))
                
                max_val = max(right_max, max_val)
                min_val = min(right_min, min_val)
            
            return [min_val, max_val, max_gap]
        
        return dfs(root)[2]
            
                