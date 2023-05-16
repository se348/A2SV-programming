# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(curr, trav, currSum, res):
            currSum += curr.val
            trav.append(curr.val)
            
            if not curr.left and not curr.right:
                if currSum == targetSum:
                    res.append(trav[:])
                    
                trav.pop()
                return
            
            if curr.left:
                dfs(curr.left, trav, currSum, res)
                
            if curr.right:
                dfs(curr.right, trav, currSum, res)
            
            trav.pop()
            
        if not root:
            return []
        
        res = []
        dfs(root, [], 0 , res)
        return res
            
            
            
            
                
        