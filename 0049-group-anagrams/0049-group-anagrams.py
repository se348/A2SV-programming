class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        
        for elem in strs:
            curr = tuple(sorted(Counter(elem).items()))
            
            arr[curr].append(elem)
        
        return arr.values()
        