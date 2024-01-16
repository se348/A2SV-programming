# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        values = []
        
        def dfs(curr_node, curr_level):
            if not curr_node:
                return True
            
            if curr_level & 1:
                
                if curr_node.val & 1 != 0:
                    return False
                
                if curr_level >= len(values):
                    values.append(curr_level)
                    
                elif values[curr_level] <= curr_node.val:
                    return False
                
            else:
                if curr_node.val & 1 == 0:
                    return False
                
                if curr_level >= len(values):
                    values.append(curr_level)
                    
                elif values[curr_level] >= curr_node.val:
                    return False
            
            values[curr_level] = curr_node.val
            
            if not dfs(curr_node.left, curr_level + 1):
                return False
                
            return dfs(curr_node.right, curr_level + 1) 
        
        return dfs(root, 0)
            