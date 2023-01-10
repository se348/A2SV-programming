class Solution:
    def recurrsion(self, top, left, right, bottom, order, matrix):   

            if bottom<top or right<left:
                return

            curr_left = left
            while curr_left <= right:
                order.append(matrix[top][curr_left])
                curr_left +=1
            
            curr_top = top + 1
            while curr_left != left and curr_top <= bottom:
                order.append(matrix[curr_top][right])
                curr_top +=1
            
            curr_right = right -1
            while curr_top != (top +1) and curr_right >= left:
                order.append(matrix[bottom][curr_right])
                curr_right -= 1
                
            curr_bottom = bottom -1
            while curr_right != (right - 1) and curr_bottom > top:
                order.append(matrix[curr_bottom][left])
                curr_bottom -= 1
                
            self.recurrsion(top+1, left+1, right-1, bottom-1, order, matrix)
            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        self.recurrsion(0, 0, len(matrix[0])-1,len(matrix)-1, order, matrix)
        return order
        