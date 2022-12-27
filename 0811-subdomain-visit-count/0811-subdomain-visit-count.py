class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = defaultdict(int)
        for word in cpdomains:
            count, domain = word.split(" ")
            llist = domain.split(".")
            if len(llist) == 2:
                res[f"{llist[0]}.{llist[1]}"] +=  int(count)
                res[f"{llist[1]}"] += int(count)
            else:
                res[f"{llist[0]}.{llist[1]}.{llist[2]}"] +=  int(count)
                res[f"{llist[1]}.{llist[2]}"] += int(count)
                res[llist[2]] +=int(count)
        ans = []
        for key, val in res.items():
            ans.append(f"{val} {key}")
        return ans
                