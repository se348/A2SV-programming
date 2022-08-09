# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        val = self.helper(root, 0, targetSum)
        return False if val is None else True
    
    def helper(self, curr, currSum=0, targetSum=0):
        curr_val= curr.val
        currSum += curr_val
        if self.hasLeftChild(curr) or self.hasRightChild(curr):
            a,b = False, False
            if self.hasLeftChild(curr):
                a= self.helper(curr.left, currSum, targetSum)
            if self.hasRightChild(curr):
                b= self.helper(curr.right, currSum, targetSum)
            if a or b:
                return True
        else:
            if currSum== targetSum:
                return True
    def hasLeftChild(self,curr: Optional[TreeNode]):
        return curr.left != None
    def hasRightChild(self,curr: Optional[TreeNode]):
        return curr.right != None
        