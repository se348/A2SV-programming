# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
        
    def deleteNode(self, root: Optional[TreeNode], key: int, prev= None) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key, root)
        elif root.val > key:
            root.left  = self.deleteNode(root.left, key, root)
        
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            curr = root.right
            while curr.left:
                curr = curr.left

            root.val = curr.val
            root.right =self.deleteNode(root.right, curr.val)
                
        return root
            