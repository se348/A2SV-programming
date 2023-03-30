# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        visited= []
        def trav(root):
            if not root:return
            trav(root.left)
            trav(root.right)
            visited.append(root.val)
        trav(root)
        visited.sort()
        tempo=visited[0]
        min_diff=math.inf
        for i in range(1, len(visited)):
            if (visited[i]-tempo)<min_diff:
                min_diff =visited[i] - tempo
            tempo = visited[i]
        return min_diff