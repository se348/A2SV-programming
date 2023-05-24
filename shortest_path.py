from collections import defaultdict, deque

def main():
    def backTrack(destination, previousTracker):
        path= [destination]
        curr = destination
        
        while previousTracker[curr] != -1:
            curr = previousTracker[curr]
            path.append(curr)
        
        path.reverse()
        print(len(path) -1)
        print(*path)
        
        
        
    n, m =list(map(int, input().split()))
    source, destionation = map(int, input().split())

    adjacencyList = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        adjacencyList[a].append(b)
        adjacencyList[b].append(a)
        
    queue = deque([source])
    visited = set([source])

    previousTracker = {source: -1}

    if source == destionation:
        print(0)
        print(source)
        return

    a = False
    while queue:
        curr = queue.popleft()
        
        for neighbor in adjacencyList[curr]:
            if neighbor not in visited:
                queue.append(neighbor)
                previousTracker[neighbor] = curr
                visited.add(neighbor)
                
            if neighbor == destionation:
                a= True
                backTrack(destionation, previousTracker)
                break    
    
    if not a:
        print(-1)
        
        
main()
