class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def constructGraph(prereq):
            graph= collections.defaultdict(list)
            for u,v in prereq:
                graph[u].append(v)
            return graph
        graph = constructGraph(prerequisites)
        source_dest={}
        for source in dict(graph).keys():
            queue= []
            visited=set()
            queue.append(source)
            visited.add(source)
            while queue:
                curr_val = queue.pop(0)
                for neigh in graph[curr_val]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)
            source_dest[source] = list(visited)
        ans=[]
        for source, dest in queries:
            if source in source_dest and  dest in source_dest[source]:
                ans.append(True)
            else:
                ans.append(False)
        return ans