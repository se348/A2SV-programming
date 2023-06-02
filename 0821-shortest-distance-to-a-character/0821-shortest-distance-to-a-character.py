class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = -inf
        res = []
        for i in range(len(s)):
            if s[i] == c: prev = i
            res.append(i - prev)

        prev = inf
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c: prev = i
            res[i] = min(res[i], prev - i)

        return res
        