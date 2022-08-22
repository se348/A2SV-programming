from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited= set()
        while queue:
            index = queue.pop()
            if arr[index] ==0:
                return True
            tempo1 = index + arr[index]
            tempo2 = index - arr[index]
            if tempo1< len(arr) and arr[tempo1]==0:
                return True
            if tempo2>=0 and arr[tempo2]==0:
                return True
            if tempo1< len(arr) and tempo1 not in visited:
                queue.append(tempo1)
                visited.add(tempo1)
            if tempo2>=0 and tempo2 not in visited:
                queue.append(tempo2)
                visited.add(tempo2)
        return False