class ThroneInheritance:

    def __init__(self, kingName: str):
        self.origin = kingName
        self.adjacencyList = defaultdict(list)
        self.adjacencyList[kingName].append(True)

    def birth(self, parentName: str, childName: str) -> None:
        self.adjacencyList[parentName].append(childName)
        self.adjacencyList[childName].append(True)

    def death(self, name: str) -> None:
        self.adjacencyList[name][0] = False

    def getInheritanceOrder(self) -> List[str]:
        
        path = []
        def dfs(curr):
            if self.adjacencyList[curr][0]:
                path.append(curr)
            
            for i in range(1, len(self.adjacencyList[curr])):
                temp = self.adjacencyList[curr][i]
                dfs(temp)
        
        dfs(self.origin)
        return path

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()