class Solution:
     def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        result = 0
        n = len(citations)
        for i in range(len(citations)):
            if citations[i] >= (n - i):
                result = max(n - i, result)

        return result