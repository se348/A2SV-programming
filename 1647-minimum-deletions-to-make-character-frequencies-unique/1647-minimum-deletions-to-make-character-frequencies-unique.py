class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s).values()
        counts_counter = Counter(counts)
        n = max(counts)
        closest_unvisiteds = []
        res = 0
        i = 0
        while i<= n:
            if i not in counts_counter:
                closest_unvisiteds.append(i)
                i += 1
            elif counts_counter[i] == 1:
                i += 1
            else:
                if closest_unvisiteds:
                    res += (i - closest_unvisiteds[-1])
                    closest_unvisiteds.pop()
                else:
                    res += (i - 0)
                counts_counter[i] -= 1

        
        return res