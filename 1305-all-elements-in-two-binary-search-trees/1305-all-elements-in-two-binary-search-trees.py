# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(curr):
            if not curr:
                return []
            
            temp = []
            
            
            prev = inorder(curr.left)
            if prev:
                temp.extend(prev)
            temp.append(curr.val)
            
            nxt= inorder(curr.right)
            if nxt:
                temp.extend(nxt)
            
            return temp
        
        
        first_arr = inorder(root1)
        second_arr = inorder(root2)
        result = []
        
        i = 0
        j = 0
        
        while i < len(first_arr) or j < len(second_arr):
            
            if j==len(second_arr) or (i < len(first_arr) and first_arr[i] <= second_arr[j]):
                result.append(first_arr[i])
                i += 1
            
            else:
                result.append(second_arr[j])
                j += 1
                
        return result