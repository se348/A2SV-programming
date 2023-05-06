"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        # print(node)
        # print(node.neighbors[0].neighbors)
        def dfs(curr):
            new_node = Node(curr.val)
            visited[curr.val] = new_node
            for temp in curr.neighbors:
                if temp.val not in visited:
                    nxt = dfs(temp)
                    nxt.neighbors.append(new_node)
                    #new_node.neighbors.append(nxt)
                else:
                    nxt = visited[temp.val]
                    nxt.neighbors.append(new_node)
                    #new_node.neighbors.append(nxt)
            return new_node
        if not node:
            return node
        if not node.neighbors:
            return Node(node.val)
        return dfs(node)