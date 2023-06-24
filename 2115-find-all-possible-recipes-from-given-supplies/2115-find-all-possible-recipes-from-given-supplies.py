class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        found = defaultdict(list)
        adjacencyList = defaultdict(list)
        queue = deque()
        visited = set()
        result = []
        recipeIdMapping = {}
        n = len(recipes)
        countDiction = defaultdict(int)
        
        
        for i in range(n):
            recipeIdMapping[recipes[i]] = i
        
        for i in range(n):
            count = len(ingredients[i])
            
            for j in range(len(ingredients[i])):
                if ingredients[i][j] not in supplies:
                    if ingredients[i][j] not in recipeIdMapping:
                        continue
                    else:
                        found[recipeIdMapping[ingredients[i][j]]].append(i)
                else:
                    count -= 1
            
            if not count:
                queue.append(i)
                visited.add(i)
            
            countDiction[i] = count
      
        while queue:
            temp = queue.popleft()
            result.append(recipes[temp])
            
            for neighbor in found[temp]:
                countDiction[neighbor] -= 1
                
                if countDiction[neighbor] == 0:
                    queue.append(neighbor)
                    
        return result
                    
