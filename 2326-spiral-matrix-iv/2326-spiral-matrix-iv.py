# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for j in range(n)] for i in range(m)]
        direction = [0, 1]
        val = [0, 0]
        curr = head
        
        inbound = lambda x, y: 0<= x <m and 0<=y <n
        
        while curr:
            mat[val[0]][val[1]] = curr.val
            
            tempo = val[0] + direction[0], val[1] + direction[1]
            if not inbound(tempo[0], tempo[1]) or mat[tempo[0]][tempo[1]]!= -1:
                direction[1] , direction[0] = -direction[0], direction[1]
            
            val[0] += direction[0]
            val[1] += direction[1]
            
            curr = curr.next
        return mat