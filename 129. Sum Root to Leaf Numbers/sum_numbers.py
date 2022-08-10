# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    sum=0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, dig_sum):
            curr_val =curr.val
            tot = f"{dig_sum}{curr_val}"
            if curr.left or curr.right:
                if curr.left:
                    dfs(curr.left, tot)
                if curr.right:
                    dfs(curr.right, tot)
            else:
                self.sum += int(tot)
        dfs(root, "")
        return self.sum
        