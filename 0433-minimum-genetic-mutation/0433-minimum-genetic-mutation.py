class Solution:
    def isDifferenceValid(self, string1, string2):
        diffCount = 0
        for i in range(8):
            if string1[i] != string2[i]:
                diffCount += 1
        
        return True if diffCount <= 1 else False
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        adjacencyList = defaultdict(set)    
        bank.append(startGene)
        
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                
                if self.isDifferenceValid(bank[i], bank[j]):
                    adjacencyList[bank[i]].add(bank[j])
                    adjacencyList[bank[j]].add(bank[i])
                    
        queue = deque([[startGene, 0]])
        visited = {startGene}
        
        while queue:
            curr_gene, curr_count = queue.popleft()
            if curr_gene == endGene:
                return curr_count
            
            for neighbor in adjacencyList[curr_gene]:
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, curr_count + 1))
                    
        return -1