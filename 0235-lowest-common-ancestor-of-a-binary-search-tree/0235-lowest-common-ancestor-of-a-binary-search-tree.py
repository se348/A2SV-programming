# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    val = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, p,q):
            if not root:
                return False, False

            left_p, left_q = find(root.left, p,q)
            right_p, right_q = find(root.right, p, q)
            
            left = left_p or right_p
            right = left_q or right_q
            
            new_l, new_r = left, right
            
            if p == root:
                new_l = True
            if q == root:
                new_r = True

            if new_l and new_r and not self.val:
                self.val = root
            
            return new_l, new_r
        
        find(root, p, q)
        return self.val
    