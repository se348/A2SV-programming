# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_llist =[]
        q_llist=[]
        def dfs(root,isP):
            if not root:
                if isP:
                    p_llist.append(None)
                else:
                    q_llist.append(None)
                return
            if isP:
                p_llist.append(root.val)
            else:
                q_llist.append(root.val)
            dfs(root.left,isP)
            dfs(root.right, isP)
            
            
        dfs(p, True)
        dfs(q, False)
        return p_llist==q_llist