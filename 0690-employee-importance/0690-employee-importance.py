"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        idDiction = {}
        def dfs(id):
            if idDiction[id].subordinates == []:
                return idDiction[id].importance
            
            count = 0
            for neighbor in idDiction[id].subordinates:
                count += dfs(neighbor)
            
            return count + idDiction[id].importance
        
        
        for employee in employees:
            idDiction[employee.id] = employee
                    
        return dfs(id)
        
        