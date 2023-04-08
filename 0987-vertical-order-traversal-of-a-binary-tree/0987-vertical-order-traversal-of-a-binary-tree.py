# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        llist =collections.defaultdict(list)
        def dfs(root, curr_x, curr_y):
            if not root:
                return
            llist[curr_x].append((-curr_y,root.val))
            dfs(root.left, curr_x-1,curr_y-1)
            dfs(root.right, curr_x+1,curr_y-1)
        dfs(root, 0,0)
        llista =[]
        val = sorted(llist.keys())
        for elem in val:
            values = llist[elem]
            values.sort()
            llista.append([va for _, va in values])
        return llista