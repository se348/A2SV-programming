# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.arr =defaultdict(lambda: -1)
        
        def dfs(root, ind):
            if not root:
                return 
            self.arr[ind] = 0
            
            dfs(root.left, 2 * ind + 1)
            dfs(root.right,2 * ind + 2)
        dfs(root, 0)
    def find(self, target: int) -> bool:
        return True if self.arr[target] == 0 else False
            
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)