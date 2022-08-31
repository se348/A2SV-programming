from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        my_list= sorted(points)
        arr=[]
        common=None
        for i in my_list:
            if arr and arr[-1][-1]>=i[0] and common and (i[0]>= common[0] and i[0]<=common[1]):
                common=list([max(common[0], i[0]),min(common[1], i[-1])])
                arr[-1][-1] =i[1]
            else:
                common=[i[0], i[1]]
                arr.append(i)
        return len(arr)
                                
                                