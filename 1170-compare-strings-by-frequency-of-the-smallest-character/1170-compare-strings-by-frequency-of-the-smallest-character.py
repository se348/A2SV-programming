class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        arrs = []
        length= len(words)
        for word in words:
            temp = Counter(word)
            curr = min(temp)
            arrs.append(temp[curr])
        
        arrs.sort()
        ans = []
        print(arrs)
        for query in queries:
            temp = Counter(query)
            curr = min(temp)

            val = temp[curr]
            
            left = 0
            right = len(arrs) -1
            res= length
            while left <= right:
                mid = (left + right) //2
                
                if arrs[mid] > val:
                    res = mid
                    right =mid -1
                
                else:
                    left = mid + 1
            
            ans.append(length - res)
            
        return ans