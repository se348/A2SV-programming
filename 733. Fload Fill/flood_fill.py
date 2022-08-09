from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_col =image[sr][sc]
        if cur_col==color:
            return image
        image[sr][sc]= color
        self.recursive_ans(image, sr, sc, cur_col, color)
        return image
    def recursive_ans(self, image, sr, sc, color_orig, color):
        for n in self.findNeighbors(image, sr,sc):
            if image[n[0]][n[1]]==color_orig:
                image[n[0]][n[1]]= color
                self.recursive_ans(image, n[0], n[1], color_orig, color)
    def findNeighbors(self, image, x,y):
        ans=[]
        if y< (len(image[0])-1):
            ans.append([x, y+1])
        if x>0:
            ans.append([x-1,y])
        if x<(len(image)-1):
            ans.append([x+1, y])
        if y>0:
            ans.append([x,y-1])
        return ans