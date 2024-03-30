class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        ay, ax = abs(ay2 - ay1), abs(ax2 - ax1)
        by, bx = abs(by2 - by1), abs(bx2 - bx1)
        
        area_a, area_b = ax * ay, bx * by
        
        int_x, int_y = 0 , 0
        
        if bx1 > ax2 or ax1 > bx2:
            pass
        else:
            int_x = min(bx2, ax2) - max(bx1, ax1)
        
        if by1 > ay2 or ay1 > by2:
            pass
        else:
            int_y = min(by2, ay2) - max(by1, ay1)
        
        
        return area_a + area_b - (int_x * int_y)
        