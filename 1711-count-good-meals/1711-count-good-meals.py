class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        two_raise =set()
        for i in range(22):
            two_raise.add(2**i)
            
        dictionary = defaultdict(int)
        res = 0
        #deliciousness.sort()
        
        for num in deliciousness:
            for n in two_raise:
                res += dictionary[n - num]
                    
            dictionary[num]+=1
            
        return (res % (10**9 + 7))