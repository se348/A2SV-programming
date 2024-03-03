# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        node_stack = []
        i = 0
        
        curr_number = 0
        curr_dash = 0
        previous_dash = 0
        
        while i < len(traversal):
            
            if traversal[i] == '-':
                if curr_dash == 0:
                    if not stack:
                        node_stack.append(TreeNode(curr_number))
                    
                    elif stack[-1][1] + 1 == previous_dash:
                        
                        curr_node = TreeNode(curr_number)
                        
                        if node_stack[-1].left:
                            node_stack[-1].right = curr_node
                        else:
                            node_stack[-1].left = curr_node
                        
                        node_stack.append(curr_node)
                    
                    else:
                        while stack[-1][1] + 1 != previous_dash:
                            node_stack.pop()
                            stack.pop()
                        
                        curr_node = TreeNode(curr_number)
                        
                        if node_stack[-1].left:
                            node_stack[-1].right = curr_node
                        else:
                            node_stack[-1].left = curr_node
                        
                        node_stack.append(curr_node)
                        
                    stack.append((curr_number, previous_dash))
                curr_number = 0
                curr_dash += 1
            
            else:
                if curr_number == 0:
                    previous_dash = curr_dash
                curr_dash = 0
                curr_number *= 10
                curr_number += int(traversal[i])
            
            i += 1
        
        if not stack:
            node_stack.append(TreeNode(curr_number))
                    
        elif stack[-1][1] + 1 == previous_dash:
                        
            curr_node = TreeNode(curr_number)

            if node_stack[-1].left:
                node_stack[-1].right = curr_node
            else:
                node_stack[-1].left = curr_node

            node_stack.append(curr_node)
                    
        else:
            while stack[-1][1] + 1 != previous_dash:
                node_stack.pop()
                stack.pop()

            curr_node = TreeNode(curr_number)

            if node_stack[-1].left:
                node_stack[-1].right = curr_node
            else:
                node_stack[-1].left = curr_node

            node_stack.append(curr_node)
            
        return node_stack[0]
        