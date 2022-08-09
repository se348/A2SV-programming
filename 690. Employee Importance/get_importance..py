# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from typing import List


class Solution:
    total=0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def mapIdToEmp(employees: List['Employee']):
            dictionary= {}
            for e in employees:
                dictionary[e.id] = e
            return dictionary
        
        mapp = mapIdToEmp(employees)
        def helper(id):
            self.total+= mapp[id].importance
            for i in mapp[id].subordinates:
                helper(i)
        helper(id)
        return self.total            
        