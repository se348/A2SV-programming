from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l =0
        r =len(height) - 1
        ans= 0
        while l<r:
            left_res = height[l]
            right_res = height[r]
            curr_area =(r-l) * min(height[l], height[r])
            ans =max(ans, curr_area)
            if height[l]< height[r]:
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:
                if height[l+1] > height[r-1]:
                    r-=1
                elif height[l+1]<= height[r-1]:
                    l+=1
        return ans