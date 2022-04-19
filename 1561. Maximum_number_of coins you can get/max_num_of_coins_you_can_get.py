class Solution:
    def maxCoins(self, piles: list) -> int:
        piles.sort()
        i=0
        j= len(piles)-1
        output =0
        while i< len(piles)/3 :
            #alices = piles[j]
            mine =piles[j-1]
            output +=mine
            #bobs =piles[i]
            i+=1
            j-=2
        return output


s= Solution()
d =s.maxCoins([9,8,7,6,5,1,2,3,4])
print(d)