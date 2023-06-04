# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjacencyList = defaultdict(list)
        
        def dfs(curr):
            if curr.left:
                adjacencyList[curr.val].append(curr.left.val)
                adjacencyList[curr.left.val].append(curr.val)
                dfs(curr.left)
                
            if curr.right:
                adjacencyList[curr.val].append(curr.right.val)
                adjacencyList[curr.right.val].append(curr.val)
                dfs(curr.right)
                
        dfs(root)
        queue = deque()
        queue.append((target.val, 0))
        count = 0
        visited = { target.val }
        
        while queue:
            if count == k:
                res= []
                for i in queue:
                    res.append(i[0])
                return res
            for i in range(len(queue)):
                curr, d = queue.popleft()
                
                for neighbor in adjacencyList[curr]:
                    if neighbor not in visited:
                        queue.append((neighbor, d + 1))
                        visited.add(neighbor)
                
            count += 1
        return []