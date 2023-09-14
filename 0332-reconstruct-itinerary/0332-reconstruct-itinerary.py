class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort()
        n = len(tickets)
        
        adjacency_list = defaultdict(list)
        
        for src, dest in tickets:
            adjacency_list[src].append([dest, 1])
            
        
        res = ["JFK"]
        def dfs(curr_node):
            if len(res) == n + 1:
                return True
            if not adjacency_list[curr_node]:
                return
            
            
            for i in range(len(adjacency_list[curr_node])):
                if adjacency_list[curr_node][i][1]:
                    adjacency_list[curr_node][i][1] = 0
                    res.append(adjacency_list[curr_node][i][0])
                    if dfs(adjacency_list[curr_node][i][0]):
                        return True
                    res.pop()
                    adjacency_list[curr_node][i][1] = 1
        
        dfs("JFK")
        return res
            
            
            