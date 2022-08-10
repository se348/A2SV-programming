# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sum= 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        def helper( curr, prep):
            pre =prep.copy()
            if len(pre)==0:
                pre = [curr.val]
            elif len(pre)==1:
                pre.append(curr.val)
            elif len(pre) == 2:
                val = pre.pop(0)
                if val%2 ==0:
                    self.sum+= curr.val
                pre.append(curr.val)
            if curr.left is not None:
                helper(curr.left, pre)
            if curr.right is not None:
                helper(curr.right, pre)
        helper(root,[])
        return self.sum
            
                